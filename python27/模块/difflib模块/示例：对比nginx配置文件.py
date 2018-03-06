# -*- coding: UTF-8 -*-
# 当我们维护多个nginx配置时，时常会对比不同版本配置文件的差异，实现代码如下：
import difflib
import sys

try:
    # 配置第一个配置文件路径参数
    # textfile1 = sys.argv[1]
    textfile1='111'
    # 配置第二个配置文件路径参数
    # textfile2 = sys.argv[2]
    textfile2='222'
except Exception as e:
    print 'Error : %s' % e
    print 'Please Usage diff_file.py filename1 filename2'
    sys.exit()


# 文件读取分隔函数
def readfile(filename):
    try:
        with open(filename, 'rb') as f:
            # 读取文件内容后进行分隔
            text = f.read().splitlines()
        return text
    except Exception as e:
        print ('Read file Error : %s' % e)
        sys.exit()


if textfile1 is None or textfile2 is None:
    print 'Usage : Usage diff_file.py filename1 filename2'
    sys.exit()

text1 = readfile(textfile1)
text2 = readfile(textfile2)
d = difflib.HtmlDiff()
with open('diffres.html','ab') as f:
    for i in  d.make_file(text1, text2):
        f.write(i)
