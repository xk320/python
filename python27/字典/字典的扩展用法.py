# -*- coding: UTF-8 -*-
#通过列表推到式来创建字典
a={num: num**2 for num in range(100)}

b ={'foo':'bar','fizz':'bazz'}
c=b.items()
print c
b['spam']='eggs'
print c