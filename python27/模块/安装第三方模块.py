# -*- coding: UTF-8 -*-

# 在python中安装第三方模块，是通过setuptools这个工具完成的，python有两个封装了setuptools的包管理工具：easy_install和pip。目前官方推
# 荐使用pip

# 举例安装一个第三方库 Python Imaging Library ，这是Python下非常强大的处理图像的工具库，一般来说第三方库都会在python官方pypi.python.org
# 网站注册，要安装一个第三方库，必须先直到该库的名称，可以在官网或者pypi上搜索，比如Python Imaging Library的名字叫PIL，安装命令是：
# pip install PIL
# 有了PIL，处理图片易如反掌。随便找个图片生成缩略图：

import Image

im = Image.open('test.png')
print im.format, im.size, im.mode
# PNG (400, 300) RGB
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')
# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：

import sys

sys.path.append('/Users/michael/my_py_scripts')
# 这种方法是在运行时修改，运行结束后失效。
# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意
# 只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。
