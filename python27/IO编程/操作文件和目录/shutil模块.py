# -*- coding: UTF-8 -*-
#但是复制文件的函数居然不再os模块中存在，原因是复制文件并非由操作系统提供的系统调用，理论上我们通过读写文件可以完成文件复制
#幸运的是shutil模块提供来copyfile()函数，还可以在shutil模块中找到很多实用的函数，它们可以看成是os模块的补充
import shutil
shutil.copyfile()
shutil.copy()
shutil.copy2()
print shutil.abspath('.')
