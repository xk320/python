#coding:UTF-8
# 操作文件和目录的函数一部分放在os中一部分放在os.path模块中，这一点要注意，
# 查看、创建和删除目录可以这么调用：
import os

# 查看当前目录的据对路径
print os.path.abspath('.')

# 在某个目录下创建一个新的目录
DIR = os.path.abspath('.')
# 拼接新目录的完整路径
DIR = os.path.join(DIR, 'haha')
# 创建一个目录
os.mkdir(DIR)
# 删除一个目录
os.rmdir(DIR)
# 两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符，
# 同样的道理，要拆分路径时，也不要直接去拆分字符串，而要通过os.path.split()函数，这样就可以把一个路径拆分成两部分，最后一部分总是最后级别
# 的目录或文件名：这种合并、拆分路径的函数并不要求目录和文件要真实存在，他们只对字符串进行操作
print os.path.split(DIR)

# 文件重命名
# os.rename('tt','aa')
# 删除文件
# os.remove('aa')

# 最后看看如何利用python的特性来过滤文件。比如我们要李处当前目录下所有目录，只需要一行代码：
print [x for x in os.listdir('/') if os.path.ismount(x)]
# 列出所有的.py文件
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

