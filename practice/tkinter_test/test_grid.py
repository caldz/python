from tkinter import *
import chad

def check():
    help(Button)
    
if __name__=='__main__':
    print('in')
    win=Tk()
    btn1=Button(win,text='press')
    btn2=Button(win,text='press')
    e1=Entry(win)
    e2=Entry(win)

    widget_list=[(btn1,0,0),(btn2,1,0),(e1,0,1),(e2,1,1)]
    for tp in widget_list:
        tp[0].grid(row=tp[1],column=tp[2])
    print('exit')
    chad.Cmd().set_focus()
    # win.mainloop()