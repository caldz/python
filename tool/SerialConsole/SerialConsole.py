import serial
import _thread
# import serial.tools.list_ports
import tkinter
import time

#sub function
def win_key_event(e):
    if e.keycode==27:
        e.widget.quit()

def text_key_event(e,s):
    if e.keycode==13:
        last_line=e.widget.get('end-1l','end')
        line_cmd=last_line.strip()
        if line_cmd!='':
            line_cmd='{}\0'.format(line_cmd)
            s.write(bytes(line_cmd,encoding='utf-8'))

def click_btn1(e,s,var):
    if var.get()!='':
        s.write(bytes(var.get(),encoding='utf-8'))
        var.set('')

def text_serial_recv_thread(s,text):
    while True:
        data_bytes=s.read()
        data_str=str(data_bytes,encoding='utf-8')
        text.configure(state='normal')
        text.insert('end',data_str)
        text.configure(state='disabled')
        text.see('end')

def entry_key_event(e,sc):
    if e.keycode==13:
        click_btn1(None,sc.s,sc.var)

class FakeSerial():
    def __init__(self,port='COM14',baudrate=115200,timeout=None):
        pass
    def write(self,data):
        print(data)
    def read(self):
        time.sleep(5)
        return bytes('hehe',encoding='utf-8')

class SerialConsole():
    def __base_config(self):
        # 选择UI模式:['sep':分离输入框和显示框,else:合并输入框和显示框]
        self.input_mode='sep'
        self.debug_mode='on'
    def __create_ui(self):
        self.scrollbar=tkinter.Scrollbar()
        self.text=tkinter.Text(self.top)
        if self.input_mode=='sep':
            self.var=tkinter.Variable()
            self.entry=tkinter.Entry(self.top,textvariable=self.var)
            self.button=tkinter.Button(self.top,text='发送')
    def __ui_config(self):
        self.text.configure(state='disabled')
    def __init__(self,top,port):
        self.__base_config()
        self.top=top
        if self.debug_mode=='on':
            self.s=FakeSerial(port=port,baudrate=115200,timeout=None)
        else:
            self.s=serial.Serial(port=port,baudrate=115200,timeout=None)
        
        self.__create_ui()
        self.__ui_config()
        self.__bind_ui()
        _thread.start_new_thread(text_serial_recv_thread,(self.s,self.text))
    
    #绑定UI
    def __bind_ui(self):
        self.top.bind('<Key>',win_key_event)
        self.text.bind('<Key>',lambda e:text_key_event(e,self.s))
        self.scrollbar.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar.set)
        if self.input_mode=='sep':
            self.button.bind('<Button-1>',lambda e:click_btn1(e,self.s,self.var))
            self.entry.bind('<Key>',lambda e:entry_key_event(e,self))
        
    def pack(self):
        self.scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.text.pack()
        if self.input_mode=='sep':
            self.entry.pack(side=tkinter.LEFT)
            self.button.pack(side=tkinter.RIGHT)
        
if __name__=='__main__':
    print('in')
    win=tkinter.Tk()
    sc=SerialConsole(top=win,port='COM14')
    sc.pack()
    win.mainloop()
    print('exit')