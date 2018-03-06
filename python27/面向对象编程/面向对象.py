# -*- coding: UTF-8 -*-
# 面向对象编程 object oriented programming 简称OO，是一种程序设计思想，OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数
# 面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数但顺序执行。为了简化程序设计，面向过程把函数继续切分子函数，即把大块函数同
# 过切割成小块函数来降低系统的复杂度。而面向对象的程序设计把计算机视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息并处理消息，计
# 算机程序的执行是一系列消息在个对象之间的传递。
# 在python中，所有的数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（class）的概念
# 举假设要处理学生的成绩表，为了表示学生的成绩，
# 面向过程的程序可以用一个dict表示：
std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 80}


# 而处理学生成绩可以通过函数实现，比如打印学生成绩：
def print_score(std):
    print '%s : %s' % (std['name'], std['score'])


print_score(std1)


# 面向对象的程序设计思想，我们是选考虑的不是程序的执行流程，而是student这种数据类型应该被视为一个对象，这个对象拥有两个属性'name'和'score'
# 如果要打印一个学生的成绩，首先必须创建出学生对应的对象，给对象发一个pring_score消息，让对象自己把自己的数据打印出来

class student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_sc(self):
        print '%s : %s' % (self.name, self.score)


# 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法（method）。面向对象的程序写出来就是这样：
bart = student('l', 97)
bart.print_sc()

# 面向对象的设计思想是从自然界中来的，因为自然界中，类和实例的概念很自然的，class是一种抽象概念，比如我们定义一个class  student，是只学生
# 这个概念，而实例（instance）则是一个个具体的student，所以面向对象的程序设计思想是抽象出class，根据class创建instance
# 面向对象的抽象程度又比函数要高，因为一个class即包含数据又包含操作方法
