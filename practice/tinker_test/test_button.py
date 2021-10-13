from tkinter import *
import os

if __name__=='__main__':
    print('in')
    win=Tk()
    win.title('Learn Tk Button')
    win.geometry('500x500+200+50')
    btn1=Button(win,
        text='退出',
        width=20,
        height=5,
        command=win.quit
        )
    btn1.pack()
    
    def func():
        print('欢迎')
    
    btn2=Button(win,
        text='点我有惊喜',
        width=40,
        height=20,
        command=func
        )
    btn2.pack()
    
    print('exit')
    # os.system("pycmd_set_focus.py pythonw.exe")
    win.mainloop()