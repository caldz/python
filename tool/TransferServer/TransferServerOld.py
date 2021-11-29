import socketserver
from socket import socket
from socket import *
import time, sys, threading, logging, json
import tcp_server_template
logging.basicConfig(format="Time[%(asctime)s] %(threadName)s[%(thread)d]: %(message)s", stream=sys.stdout, level=logging.INFO)

class MyData:
    sm_stat='wait_reg'
    reg_address=('',12345)
md=MyData()

class TranferServerHandler(tcp_server_template.ServerHandlerTemplate):
    def setup(self):
        global md
        super().setup() 
        if md.sm_stat=='transfer':
            try:
                self.client_sock=socket(AF_INET,SOCK_STREAM)
                self.client_sock.connect(md.reg_address)
            except:
                print('Unexpected Error:{}'.format(sys.exc_info()[0]))
                
    def finish(self):
        global md
        super().finish()
        if md.sm_stat=='transfer':
            self.client_sock.close()
        elif md.sm_stat=='mid':
            print('reg {} success'.format(md.reg_address))
            md.sm_stat='transfer'
            
    def __proc_main(self,data):
        global md
        if md.sm_stat=='wait_reg':
            self.__proc_wait_reg(data)
        elif md.sm_stat=='transfer':
            self.__proc_transfer(data)
            
    def __proc_wait_reg(self,data):
        global md
        try:
            json_str=str(data,encoding='utf-8')
            json_data=json.loads(json_str)
            print(json_data)
            md.reg_address=(self.client_address[0],json_data['server_port'])
            md.sm_stat='mid'
            self.request.send('reg ok'.encode(encoding='utf-8'))
        except:
            print('Unexpected Error:{}, disconnect {}'.format(sys.exc_info()[0],self.client_address))
            self.request.send('Invalid Data'.encode(encoding='utf-8'))
            self.request.close()
    def __proc_transfer(self,data):
        global md
        try:
            self.client_sock.send(data)
        except:
            print('Unexpected Error:{}'.format(sys.exc_info()[0]))
        
    def proc_recv_data(self,data):
        self.__proc_main(data)

if __name__ == '__main__':
    server_ip='172.16.24.5'
    server_port=9999
    tcp_server_template.run_server(server_ip,server_port,TranferServerHandler)
    print('exit')