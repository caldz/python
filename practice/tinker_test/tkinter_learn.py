from tkinter import *
import os
if __name__ == '__main__':
    print('in')
    w = Tk()
    w.title('Tkinter Learn')
    w.geometry('500x300')
    l = Label(w,text='你好！',bg='green',font=('Arial,12'),width=30,height=2)
    # chad.pycmd_set_focus.cmd_set_focus('pythonw.exe')
    os.system('pycmd_set_focus.py pythonw.exe')
    print('exit')   