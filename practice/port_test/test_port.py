import chad
import serial
import serial.tools.list_ports
from serial import Serial

def get_com_list():
    port_list=list(serial.tools.list_ports.comports())
    for port in port_list:
        print(port)
    return port_list

def always_recv_com():
    s=Serial(port='COM3',baudrate=115200,timeout=None)
    while True:
        data=s.read()
        s1=str(data,encoding='utf-8')
        print(s1,end='')
    print(s)

if __name__=='__main__':
    print('in')
    port_list=get_com_list()
    always_recv_com()
    print('exit')