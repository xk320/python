# -*- coding: UTF-8 -*-
import logging

import pymysql, configparser, time, threading
from DBUtils.PooledDB import PooledDB, PooledDBError

'''
PooledDB的参数：
1. mincached，最少的空闲连接数，如果空闲连接数小于这个数，pool会创建一个新的连接
2. maxcached，最大的空闲连接数，如果空闲连接数大于这个数，pool会关闭空闲连接
3. maxconnections，最大的连接数，
4. blocking，当连接数达到最大的连接数时，在请求连接的时候，如果这个值是True，请求连接的程序会一直等待，直到当前连接数小于最大连接数，如果
   这个值是False，会报错，
5. maxshared 当连接数达到这个数，新请求的连接会分享已经分配出去的连接
'''

logging.basicConfig()
logging.basicConfig(level=logging.DEBUG)
def create_engine():
    # 初始化数据库连接函数
    myconf = configparser.ConfigParser()
    myconf.read('../conf/config.yml')
    HOST = myconf.get('DB', 'HOST')
    PORT = int(myconf.get('DB', 'PORT'))
    DATABASE = myconf.get('DB', 'DATABASE')
    USERNAME = myconf.get('DB', 'USERNAME')
    PASSWORD = myconf.get('DB', 'PASSWORD')
    MINPOOL = int(myconf.get('DB', 'MINPOOL'))
    MaxConnecTions = int(myconf.get('DB', 'MaxConnecTions'))
    return PooledDB(pymysql, mincached=MINPOOL, maxcached=MaxConnecTions, maxconnections=MaxConnecTions, host=HOST,
                    port=PORT,user=USERNAME, passwd=PASSWORD, db=DATABASE,blocking=True)


engine = create_engine()

def _profiling(starttime,sql=''):
    t=time.time()-starttime
    logging.info('SQL Runtime  %.2fs: %s' % (t,sql))


def conn(i):
    global engine
    print(i)
    # 当连接池满了新线程进入等待,每1秒尝试一次获取连接
    tcon = engine.connection()
    sql=''
    cur = tcon.cursor()
    runtime=time.time()
    print('DB Pool %s....' % i)
    time.sleep(3)
    _profiling(runtime,sql=sql)
    cur.close()


for i in range(0, 11):
    threadlist = []
    t = threading.Thread(target=conn, args=(i,))
    threadlist.append(t)
    t.start()

for t in threadlist:
    t.join()
engine.close()
