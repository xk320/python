# -*- coding: UTF-8 -*-
import Tkinter,tkMessageBox
class Application(Tkinter.Frame):
    def __init__(self,master=None):
        Tkinter.Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput=Tkinter.Entry(self)
        self.nameInput.pack()
        self.alertButton=Tkinter.Button(text='确定',command=self.hello)
        self.alertButton.pack()
        self.quitButton=Tkinter.Button(text='退出',command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name=self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message','Hello, %s' % name)
#当用户点击按钮时，出发hello()，通过self。nameInput.get()获取用户输入文本后，使用tkMessageBox.showinfo()可以弹出消息对话框
APP=Application()
APP.master.title('测试文本框')
APP.mainloop()
