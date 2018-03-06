# -*- coding: UTF-8 -*-
# 在程序运行的过程中，所有的变量都存在内存中，比如定义一个dict
d = dict(name='Bob', age=20, score=18)
# 可以随时修改变量，比如把name改成bill，但是一旦程序结束来，变量所占内存就被操作系统全部回收，如果没有把修改后但bill存到磁盘上，下次重启程
# 序变量又被初始化为Bob，我们把变量从内存中变成可存储或者传输但过程成为序列化，在python中叫pickling，在其他语言中也被成为serialization
# marshalling、flattening等等，都是一个意思
# 序列化后，就可以把序列化后内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读入内存称之为反序列化，即unpickling
# python提供两个模块来实现序列化：cPickle和pickle，这两个模块的功能一样，区别在于cPickle是C语言写的速度块。用的时候，先尝试导入cPickle，
# 如果失败，再导入pickle：
try:
    import cPickle as pickle
except ImportError:
    import pickle

# 首先我们尝试把一个对象序列化写入文件
print pickle.dumps(d)
# pickle.dumps()方法是把任意对象序列化成一个str，然后就可以把这个str写入文件，后者用另外一个方法pickle.dump()直接把对象序列化后写入一个
# file-like object
with open('tt', 'wb') as f:
    pickle.dump(d, f)

    # 当我们要把对象从磁盘读到内存时，可以先把内容读到一个str，然后用pickle.loads()方法反序列化对象，也可以直接用pickle.load()方法从一个
    # file-like object中直接反序列化出对象
    # try:
    #     import cPickle as pickle
    # except ImportError:
    #     import pickle
    #
    # #pickle.load()方法直接从file-like object中反序列化对象
    # with open('tt','r') as f :
    #     d = pickle.load(f)
    # print d
    #
    # #pickle.loads()方法从str反序列化对象
    # with open('tt','r') as f:
    #     a=f.read()
    # d=pickle.loads(a)
    # print '-'*80
    # print pickle.load(f)
    #
    # Pickle的问题和所有其他变成语言特有的序列化问题一样，就是只能用于python，并且不同版本的python彼此都不兼容，因此只能保存那些不重要的数据
