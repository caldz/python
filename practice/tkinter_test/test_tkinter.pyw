from tkinter import (
    Frame, LEFT, YES, BOTTOM, Entry, TOP, Button, Tk, X,
    Toplevel, RIGHT, Y, END, Listbox, BOTH, Scrollbar,
)
if __name__ == '__main__':
    print('start')
    root=Tk()
    root.title('hehe')
    root.geometry('200x200')
    btn=Button(root,width=10,height=8,text='press')
    btn.pack()
    root.mainloop()
    print('exit')
