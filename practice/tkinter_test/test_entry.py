from tkinter import *


def test_tk():
    win=Tk()
    win.title('输入框测试')
    win.geometry('500x500+250+150')
    e1=Variable()
    entry=Entry(win,textvariable=e1)
    entry.pack()
    e1.set('请输入内容')
    print(e1.get())
    def func():
        print(e1.get())
    button=Button(win,text='提交',command=func)
    button.pack()
    win.mainloop()
    
if __name__=='__main__':
    test_tk()