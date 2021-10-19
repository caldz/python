import tkinter
import re

def text_key_event(e,text):
    if e.keycode==13:
        last_line=text.get('end-1l','end')
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
    text.bind('<Key>',lambda e:text_key_event(e,text))
    scroll=tkinter.Scrollbar()
        
    #关联滚动条和文字框
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    
    
    #布局滚动条和文字框
    scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
    text.pack()
    
    for i in range(20):
        text.insert('end','{}\n'.format(i))
        print(i)
    #把光标和屏幕移到文本末端
    text.see('end')
    
    win.mainloop()
    print('exit')