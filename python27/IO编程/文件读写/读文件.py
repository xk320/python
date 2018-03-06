#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 要以读文件的模式打开一个文件对象，使用python内置的open()函数，传入文件名和标识符：
f = open(u'概述', 'r')
# 标识符r标识读，这样我们就成功打开了一个文件
# 如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在
# 如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，python吧内容读到内存中，用一个str对象表示
print f.read()
f.close()
# 最后一步调用close()方法关闭文件，一旦出错，后面的f.close()就不会调用，所以为了保证无论是否出错都能正确的关闭文件，我们
# 可以使用try:... finally来实现：
try:
    f = open(u'概述', 'r')
    print f.read()
finally:
    f.close()

# 但是每次这么写是在太繁琐，所以python引入了with语句来自动帮我们调用close()方法
with open(u'概述', 'r') as f:
    print f.read()
    print '-' * 42

# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多
# 读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，
# 要根据需要决定怎么调用。
with open(u'概述', 'r') as f:
    for i in f:
        print i.strip('')  # 把末尾的\n删掉

# file-like object
# 像open()函数返回这种有read()方法的对象，在python中统称为file-like objet，除了file外，还可以是内存的字节流、网络流、自定义流等等。
# file-like object不要求从特定的类继承，只要写一个read()方法就行。StringIO就是在内存中创建的file-like Object，通常做临时模块

# 二进制文件
# 前面将的默认都是读取文本文件，并且是ASCII编码的文本文件，要读取二进制文件，比如图片、视频等等，用rb模式打开文件即可：

f = open('0.jpeg', 'rb')
print f.read()
f.close()
# 字符编码
# 要读取非ASCII编码的文本文件，就必须以二进制模式打开，在解码，比如UTF-8编码文件
with open(u'概述', 'rb') as f:
    print f.read().decode('utf8')

# 如果每次都这么手动转换编码很麻烦，python提供类一个codecs模块帮我们在读文件都时候自动转换编码
import codecs

with codecs.open(u'概述','r','utf8') as f:
    print f.read()
