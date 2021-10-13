import tkinter as tk

class App(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there=tk.Button(self)
        self.hi_there['text']='hello world\n(click me)'
        self.hi_there['command']=self.say_hi
        self.hi_there.pack(side='top')
        self.quit=tk.Button(self,text='quit',fg='red',command=self.master.destroy)
        self.quit.pack(side='bottom')

    def say_hi(self):
        print('hi there,everyone!')

if __name__ == '__main__':
    root=tk.Tk()
    app=App(master=root)
    app.mainloop()
        
