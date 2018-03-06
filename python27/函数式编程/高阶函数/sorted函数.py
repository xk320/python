# -*- coding: UTF-8 -*-
# 排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小，如果数字
# 我们可以直接比较，但是如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必
# 须通过函数抽象出来，通常规定，对于两个元素x和y，如果认为x<y,则返回-1，如果x==y，则返回0，如果认为
# x>y,则返回1，这样排序算法就不用关心具体的比较过程，而是根据比较结果直接排序。
# python内置的sorted（）函数就可以对list进行排序：
print sorted([36, 5, 12, 9, 21])
print sorted(['a', 'n', 'm', 'g'])


# sorted（）函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义排序。比如，如果要倒序排序，就可以自定
# 义一个reversed_cmp函数：
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36, 5, 12, 9, 21],reversed_cmp)

#sorted（）方法即可以保留原列表，有能得到已经排序好对列表
a = [1,2,5,6,4,9]
b = sorted(a)
print a,'\n',b