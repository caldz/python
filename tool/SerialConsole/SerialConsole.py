import serial
import _thread
# import serial.tools.list_ports
import tkinter

#sun function
def click_btn1(s,var):
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
        #serial init
        self.s=serial.Serial(port=port,baudrate=115200,timeout=None)
        
        #ui init
        self.text=tkinter.Text(win)
        self.var=tkinter.Variable()
        self.entry=tkinter.Entry(win,textvariable=self.var)
        self.button=tkinter.Button(win,command=lambda:click_btn1(self.s,self.var),text='发送')
        
        _thread.start_new_thread(text_serial_recv_thread,(self.s,self.text))
        
    def pack(self):
        self.text.pack()
        self.entry.pack(side=tkinter.LEFT)
        self.button.pack(side=tkinter.RIGHT)
        
if __name__=='__main__':
    print('in')
    win=tkinter.Tk()
    sc=SerialConsole(win=win,port='COM14')
    sc.pack()
    win.mainloop()
    print('exit')