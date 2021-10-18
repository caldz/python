import tkinter


def text_key_event(event,text):
    print('keycode={}'.format(event.keycode))

def win_key_event(event,win):
    # print('keycode={}'.format(event.keycode))
    if (event.keycode==27):
        win.quit()
if __name__=='__main__':
    print('in')
    win=tkinter.Tk()
    win.bind('<Key>',lambda event:win_key_event(event,win))

    text=tkinter.Text(win)
    scroll=tkinter.Scrollbar()
    
    #关联滚动条和文字框
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    
    #布局滚动条和文字框
    scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
    text.pack()
    text.bind('<Key>',lambda event:text_key_event(event,text))
    help(text)
    
    for i in range(20):
        text.insert('end','{}\n'.format(i))
        print(i)
    #把光标和屏幕移到文本末端
    text.see('end')
    win.mainloop()
    print('exit')