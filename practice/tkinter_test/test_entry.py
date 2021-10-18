import tkinter

def event_key(event):
    print('keycode={}'.format(event.keycode))

def test_tk():
    win=tkinter.Tk()
    win.title('输入框测试')
    win.geometry('500x500+250+150')
    e1=tkinter.Variable()
    entry=tkinter.Entry(win,textvariable=e1)
    entry.bind('<Key>',event_key)
    entry.pack()
    e1.set('请输入内容')
    print(e1.get())
    def func():
        print(e1.get())
    button=tkinter.Button(win,text='提交',command=func)
    button.pack()
    win.mainloop()
    
if __name__=='__main__':
    test_tk()