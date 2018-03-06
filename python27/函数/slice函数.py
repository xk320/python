# -*- coding: UTF-8 -*-

#slice()函数实现切片对象，主要用于在切片操作函数里的参数传递

#语法
#class slice(stop)
#class sliec(start,stop[,step])
#start 起始位置  stop  结束位置  step 间距

#返回值     返回一个切片对象

#实例     展示slice的使用方法
myslice=slice(5)  #设置截取5个元素的切片
print myslice
arr=range(10)
print arr
print arr[myslice]  #截取5个元素