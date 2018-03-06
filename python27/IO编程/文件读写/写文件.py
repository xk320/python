# -*- coding: UTF-8 -*-
# 写文件与读文件一样，区别在于调用open()函数时，传入标识符w或者wb表示写文本文件或者二进制文件：
f = open('tt', 'w')
f.write('Hello World!')
f.close()
# 可以反复调用write来写文件，但是务必要调用close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空
# 闲的时候慢慢写入，只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘，忘记调用close()的后果是数据可能只写了一部分到磁盘
# 剩下的丢失了，还是用with语句保险：
with open('tt', 'w') as f:
    f.write('哈哈哈')

# 将特定的文本写入文件：
import codecs

with codecs.open('tt', 'w') as f:
    f.write('哈哈')

with codecs.open('tt', 'a') as f:
    f.write('heheh')

# 在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。
