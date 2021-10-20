import serial
import _thread
# import serial.tools.list_ports
import tkinter

#sun function
def win_key_event(e):
    if e.keycode==27:
        e.widget.quit()

def text_key_event(e,s):
    if e.keycode==13:
        last_line=e.widget.get('end-1l','end')
        line_cmd=last_line.strip()
        if line_cmd!='':
            print(line_cmd)
            line_cmd='{}\0'.format(line_cmd)
            print(bytes(line_cmd,encoding='utf-8'))
            s.write(bytes(line_cmd,encoding='utf-8'))

def click_btn1(e,s,var):
    print('hehe')
    s.write(bytes(var.get(),encoding='utf-8'))

def text_serial_recv_thread(s,text):
    while True:
        data_bytes=s.read()
        data_str=str(data_bytes,encoding='utf-8')
        print(data_str,end='')
        text.insert('end',data_str)
        text.see('end')

class SerialConsole():
    def __init__(self,win,port):
        win.bind('<Key>',win_key_event)
    
        #初始化配置信息
        self.input_mode=''
        
        #创建串口对象
        self.s=serial.Serial(port=port,baudrate=115200,timeout=None)
        
        #创建UI组件
        self.scrollbar=tkinter.Scrollbar()
        self.text=tkinter.Text(win)
        if self.input_mode=='sep':
            self.var=tkinter.Variable()
            self.entry=tkinter.Entry(win,textvariable=self.var)
            self.button=tkinter.Button(win,text='发送')
        
        self.ui_bind()
        _thread.start_new_thread(text_serial_recv_thread,(self.s,self.text))
    
    #绑定UI
    def ui_bind(self):
        self.text.bind('<Key>',lambda e:text_key_event(e,self.s))
        self.scrollbar.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar.set)
        if self.input_mode=='sep':
            self.button.bind('<Button-1>',lambda e:click_btn1(e,self.s,self.var))
        
    def pack(self):
        self.scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.text.pack()
        if self.input_mode=='sep':
            self.entry.pack(side=tkinter.LEFT)
            self.button.pack(side=tkinter.RIGHT)
        
if __name__=='__main__':
    print('in')
    win=tkinter.Tk()
    sc=SerialConsole(win=win,port='COM14')
    sc.pack()
    win.mainloop()
    print('exit')