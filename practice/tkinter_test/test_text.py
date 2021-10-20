import tkinter

def text_key_event(e):
    if e.keycode==13:
        last_line=e.widget.get('end-1l','end')
        line_cmd=last_line.strip()
        if line_cmd!='':
            print(line_cmd)

def win_key_event(e):
    if e.keycode==27:
        e.widget.quit()

if __name__=='__main__':
    print('in')
    win=tkinter.Tk()
    win.bind('<Key>',win_key_event)


    text=tkinter.Text(win)
    text.bind('<Key>',lambda e:text_key_event(e))
    scrollbar=tkinter.Scrollbar()
        
    #关联滚动条和文字框
    scrollbar.config(command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    
    
    #布局滚动条和文字框
    scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
    text.pack()
    
    for i in range(20):
        text.insert('end','{}\n'.format(i))
        print(i)
    #把光标和屏幕移到文本末端
    text.see('end')
    
    win.mainloop()
    print('exit')