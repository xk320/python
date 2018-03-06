# -*- coding: UTF-8 -*-
#python内建的filter（）函数用于过滤序列和map相似，filter也可以接收一个函数和序列，不同之处在于filter把
#传入的函数一次作用与每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
#例如，在一个list中删掉偶数值保留奇数
def is_odd(n):
    return n % 2 ==1
print filter(is_odd,[1,2,3,4,5,6,7])

#把一个序列中的空字符删除掉
def not_empty(s):
    return s and s.strip()
print filter(not_empty,['a',' ','b'])