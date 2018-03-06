# -*- coding: UTF-8 -*-
#通过difflib模块实现文件内容差异对比，标准库模块无需安装
import difflib
#对比两个字符串的差异
text1='''
test:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
'''
#以行进行分隔，以便进行对比
text1_lines=text1.splitlines()
text2='''
test:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5
'''
text2_lines=text2.splitlines()
#创建一个Differ()对象
d=difflib.Differ()
diff=d.compare(text1_lines,text2_lines)
print '\n'.join(diff)
#本实例采用Differ()类对两个字符串进行比较，另外difflib的SequenceMatcher()类支持任意类型序列的比较，htmlDiff()类支持将比较结果输出为
#HTML格式。
# - 表示包含在第一个序列中，不包含在第二个序列中
# + 表示包含的第二个序列中，不包含在第一个序列中
# ''表示两个序列一致
# ？ 表示两个序列行存在增量差异
# ^ 标志两个序列存在差异的字符

#生成美观的对比HTML文档
#采用HtmlDiff()类的make_file()方法就可以生成美观的HTML文档，
dd=difflib.HtmlDiff()

with open('test.html','a') as f:
    for line in dd.make_file(text2_lines,text1_lines):
        f.write(line)