from tkinter import *


if __name__ == '__main__':
    def test():
        root = Tk()
        root.geometry('500x500')
        btn1=Button(root,text='test1')
        btn2=Button(root,text='test2')
        btn3=Button(root,text='test3')
        btn4=Button(root,text='test4')
        btn1.pack(side='left', expand='no', anchor='w', fill='y', padx=5, pady=5)
        btn2.pack(side='bottom')
        btn3.pack(side='top')
        # btn1.pack(side='left', expand='no', fill='y')
        # btn2.pack(side='top', fill='x')
        # btn3.pack(side='right', expand='yes', fill='both')
        root.mainloop()
    
    test()