#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢，因为list是线性存储，数据量大的时候，插入和删除效率很低
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
import collections

q = collections.deque([1, 2, 3, 4])
q.append(5)
q.appendleft(6)
print q
# deque除了实现list的append和pop外，还支持appendleft和popleft，这样就非常高效地往头部添加或删除元素。
