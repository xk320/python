# -*- coding: UTF-8 -*-
# 在一个web APP中，所有数据，包括用户信息、发布的日志、评论等，都存储在数据库中，在awesome-pyton-app中，我们选择mysql作为数据库
# web app 里面又很多地方都要访问数据库，访问数据库需要创建数据库连接、游标对象，然后执行SQL语句，最后处理异常、清理资源。这些访问数据库代码
# 如果分散到每个函数中，势必无法维护，也不利于代码复用。
# 此外，在一个web app中，又多个用户会同时访问，系统以多进程或多线程的模式来处理每个用户的请求，假设以多线程为例，每个线程在数据库访问时，都
# 必须创建仅属于自己的连接，对别的线程不可见，否则，就会造成数据库操作混乱
# 所以我们还要创建一个简单可靠的数据库访问模型，在一个线程中能够安全又简单的操作数据库
# 为什么不选择SQLAlchemy？SQLAlchemy太庞大，过渡地面向对象设计导致API太复杂
# 所以我们决定自己设计一个封装基本的select、insert、update和delete的db模块：transwarp.db

# 设计 db 接口
# 设计底层模块的原则是,根据上层调用者设计简单易用的 API 接口,然后实现模块内部代码
# 假设 transwarp.db 模块已经编写完毕,我们希望以这样的方式来调用他:
# 首先初始化数据库连接信息,通过 create_engine() 函数:
from transwarp import db
db.create_engine(user='root',password='password',database='test',host='127.0.0.1',port=3306)
# 然后就可以直接操作 SQL 了
# 如果需要做一个查询,可以直接调用 select() 方法,返回的是 list, 每个元素是用 dict 标识的对应的行
users=db.select('select * from suer')
# users=>
# [
#   {"id":1,"name":"Jack"},
#   {"id":2,"name":"Bob"}
# ]
# 如果要执行 insert update deletecaozuo ,执行 update() 方法,返回受影响的行数
# n=db.update('update users set name = "Lily" where id in (?,?',4,5)
# update() 函数签名为     update(slq,*args)
# 统一用?作为占位符,并传入可变参数来绑定,从根本上避免 SQL 注入共计
# 每个 select() 和 update() 调用,都隐含地自动打开并关闭了数据库连接,这样上层调用者完全不必关心数据库地层连接
# 但是,如果要在一个数据库连接里执行多个 SQL 语句怎么办?我们用一个 with 语句实现:
with db.connection():
  db.select('...')
  db.select('...')
  db.select('...')
# 如果要在一个数据库失误中执行多个SQL 语句怎么办?我们还是用一个 with 语句实现:
with db.transaction():
  db.select('...')
  db.update('...')
  db.insert('...')
#实现 DB 模块
#由于模块是全局对象,模块变量是全局唯一变量,有两个重要的变量:
#代码在 operational_training 中编写
# -*- coding: UTF-8 -*-
import threading


# 数据库引擎对象
class _Engine(object):
    def __init__(self, connect):
        self._connect = connect

    def connect(self):
        return self._connect()


engine = None


# 持有数据库连接的上下文对象
class _DbCtx(threading.loacl):
    def __init__(self):
        super(_DbCtx, self).__init__()
        self.connection = None
        self.transactions = 0

    def is_init(self):
        return not self.connection is None

    def init(self):
        self.connection = _LasyConnection()
        self.transactions = 0

    def cleanup(self):
        self.connection.cleanup()
        self.connection = None

    def cursor(self):
        return self.connection.cursor()


_db_ctx = _DbCtx()


# 由于_ db_ctx 是 threadlocal 对象所以它持有的数据库连接对于每个线程看到的都是不一样的,任何一个线程都无法访问到其他线程持有的数据库连接
# 有了这两个全局变量,我们继续实现数据库连接的上下文,目的是自动获取和释放连接

class _ConnectionCtx(object):
    def __enter__(self):
        global _db_ctx
        self.should.cleanup = False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should.cleanup = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        global _db_ctx
        if self.should.cleanup:
            _db_ctx.cleanup()


# 定义__ enter__{} 和__ exit__()的对象可以用于 with 语句,确保任何情况下__ exit__() 方法可以被调用
def connection():
    return _ConnectionCtx()

# 把_ ConnectionCtx 的作用域作用到一个函数调用上,可以这么写:
with connection():
    do_some_db_operation()
#但更加简单的写法是写个@ decorator
@with_connection
def do_some_db_operation():
    pass
#这样我们实现 select() 和 update()方法就更简单了
@with_connection
def select(sql,*args):
    pass
@with_connection
def update(sql,*args):
    pass
#注意到 Connection 对象是存储在 _DbCtx这个 threadlocal 对象里的,因此嵌套使用 with_connection() 也没问题. _DbCtx 永远检测当前是否
#已存在 Connection, 如果存在直接使用,如果不存在则打开一个新的 Connection
#对于 transaction 也是类似的, with_transaction() 定义了一个数据库事务:
with db.transaction():
    db.select('...')
    db.update('...')
    db.update('...')
# 函数作用域的事务也有一个简化的@decorator：
#
@with_transaction
def do_in_transaction():
    pass
#事务嵌套比 Connection 嵌套复杂一点,因为事务嵌套需要计数,没遇到一层嵌套就+1,离开一层嵌套就-1,最后到0时提交事务
class _TransactionCtx(object):
    def __enter__(self):
        global _db_ctx
        self.should.cleanup=False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should.cleanup=True
        _db_ctx.transactions=_db_ctx.transactions+1
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        global _db_ctx
        _db_ctx.transactions = _db_ctx.transactions - 1
        try:
            if _db_ctx.transactions==0:
                if exc_type is None:
                    self.commit()
                else:
                    self.rollback()
        finally:
            if self.should.cleanup:
                _db_ctx.cleanup()

    def commit(self):
        global _db_ctx
        try:
            _db_ctx.connection.commit()
        except:
            _db_ctx.connection.rollback()
            raise
    def rollback(self):
        global _db_ctx
        _db_ctx.connection.rollback()
