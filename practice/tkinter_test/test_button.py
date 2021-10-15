from tkinter import *
import os
import chad
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
    
    def event_enter(event):
        print('enter:<x={},y={}>'.format(event.x,event.y))
    def event_leave(event):
        print('leave:<x={},y={}>'.format(event.x,event.y))
    def event_double_click(event):
        print('double_click:<x={},y={}>'.format(event.x,event.y))
    def func():
        print('欢迎')
    
    btn2=Button(win,
        text='点我有惊喜',
        width=40,
        height=5,
        command=func
        )
    btn2.bind('<Double-Button-1>',event_double_click)
    btn2.bind('<Enter>',event_leave)
    btn2.bind('<Leave>',event_leave)
    btn2.pack()
    
    print('exit')
    # chad.Cmd().set_focus('pythonw.exe')
    # os.system('pycmd_set_focus.py pythonw.exe')
    win.mainloop()