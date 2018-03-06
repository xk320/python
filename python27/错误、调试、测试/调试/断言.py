#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#凡是用print来辅助查看的地方，都可以用断言（assert）来替代：
def foo(s):
    n = int(s)
    assert n !=0,'n is zero'
    return 10 /n
def main():
    foo('0')
main()
#assert的意思是表达式n!=0应该是true，否则，后面的代码就会出错
#如果断言失败，assert语句本身就会抛出assertionerror：
#程序中如果导出充斥着assert，和print相比也好不到哪去，不过启动平python解释器时，可以用-0参数来关闭assert
#关闭后，你可以吧所有的assert语句当成pass来看