from tkinter import *

class VendingMachine:
    def grid_init(self,top):
        fm1=Frame(top)
        btn1=Button(fm1,text='TFirst').grid(row=0,column=0)
        btn1=Button(fm1,text='TSecond').grid(row=0,column=1)
        btn1=Button(fm1,text='TRight').grid(row=0,column=2)
        fm1.grid(row=0,column=0)
        
        fm2=Frame(top)
        Button(fm2,text='LFirst').grid(row=0,column=0)
        Button(fm2,text='LSecond').grid(row=1,column=1)
        Button(fm2,text='LThird').grid(row=2,column=2)
        fm2.grid(row=1,column=0)
        
    def pack_init(self,top):
        fm1=Frame(top)
        btn1=Button(fm1,text='TFirst').pack(side=TOP, anchor=W, fill=X, expand=YES)
        btn1=Button(fm1,text='TSecond').pack(side=TOP, anchor=W, fill=X, expand=YES)
        btn1=Button(fm1,text='TRight').pack(side=TOP, anchor=W, fill=X, expand=YES)
        
        fm1.pack(side=LEFT,anchor=NW)
        fm2=Frame(top)
        Button(fm2,text='LFirst').pack(side=LEFT)
        Button(fm2,text='LSecond').pack(side=LEFT)
        Button(fm2,text='LThird').pack(side=LEFT)
        fm2.pack(side=LEFT,anchor=SE)
        
    def __init__(self,top):
        self.grid_init(top)
        
if __name__=='__main__':
    print('in')
    root=Tk()
    root.geometry('500x500+0+0')
    vm=VendingMachine(root)
    root.mainloop()
    print('exit')