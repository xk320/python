# -*- coding: UTF-8 -*-

# 别名
#导入模块时，还可以使用别名，这样可以在运行是根据当前环境选择最合适的模块，比如python标准库一般会提供StringIO和cStringIO两个库，这两个库
# 的接口和功能是一样的，但是cStringIO是C写的，速度更快，所以你经常看到这样的写法：
try:
    import cStringIO as StringIS
except ImportError:
    import StringIO

#这样可以优先导入cStringIO，如果有些平台不提供cStringIO还可以降级导使用StringIO。导入cStringIO时，用 import...as...指定别名StringIO
#因此，后续代码引用StringIO即可正常工作

try:
    import json
except ImportError:
    import simplejson as json

#由于python是动态语言，函数签名一致接口就一样，因此无论导入那个模块后续代码都可以正常工作

