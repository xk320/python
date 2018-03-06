# -*- coding: UTF-8 -*-
# 使用Tkinter十分简单，编写一个Hello world实例
import Tkinter


# 第一步是从Frame派生出一个Application类，这是所有Widget的父容器
class Application(Tkinter.Frame):
    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Tkinter.Label(self, text='Hello world!')
        self.helloLabel.pack()
        self.quitButton = Tkinter.Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()


# 在GUI中，每个button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树
# pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局
# 在createWidget()方法中，我们创建类一个Label和一个Button，当Button被点击时，出发self.quit()使程序退出。
# 最后，实例话Application，并启动消息循环
app = Application()
app.master.title('Hello')
app.mainloop()
# GUI程序的祝线程负责监听来自操作系统的消息，并依次处理每一条消息，因此如果消息非常耗时，就需要在新的线程处理。
