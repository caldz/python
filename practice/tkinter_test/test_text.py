import tkinter


if __name__=='__main__':
    print('in')
    win=tkinter.Tk()
    text=tkinter.Text(win)
    scroll=tkinter.Scrollbar()
    
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    help(text.config)
    text.config(wrap=tkinter.WORD)
    text.insert('insert','1111')
    text.insert('end','3333')
    text.insert('0.0','2222')
    
    
    scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
    text.pack()
    
    for i in range(50):
        text.insert('end','{}\n'.format(i))
        print(i)
    #把光标和屏幕移到文本末端
    text.see('end')
    win.mainloop()
    print('exit')