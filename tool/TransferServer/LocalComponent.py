from socket import *
import sys,json,base64
import tcp_server_template
import _thread
import traceback
    
def tcpsock_send_dict_data(tcpsock,dict_data):
    json_str=json.dumps(dict_data)
    tcpsock.send(json_str.encode(encoding='utf-8'))

class LcRoute:
    def __init__(self):
        self.sock=None
        self.real_address=None

class LocalComponent:
    
    def __init__(self,target_server_address):
        self.lc_routes=set()
        self.transfer_server_addr=None
        self.target_server_addr=target_server_address
    def proc_cmd_connect(self,dict_data):
        print('todo connect')
        lcr=LcRoute()
        lcr.sock=socket(AF_INET,SOCK_STREAM)
        lcr.sock.connect(self.target_server_addr)
        lcr.real_address=dict_data['client_address']
        self.lc_routes.add(lcr)
    def proc_cmd_disconnect(self,dict_data):
        print('todo disconnect')
        for lcr in self.lc_routes:
            print(lcr.real_address, lcr.sock)
    def proc_cmd_send(self,dict_data):
        print('todo send')
        str_base64_data=dict_data['base64_data']
        data=base64.b64decode(str_base64_data)
        print(data)
    def proc_parse_data(self,dict_data):
        print(dict_data)
        cmd=dict_data
        try:
            if dict_data['cmd']=='sc_connect':
                self.proc_cmd_connect(dict_data)
            elif dict_data['cmd']=='sc_disconnect':
                self.proc_cmd_disconnect(dict_data)
            elif dict_data['cmd']=='sc_send':
                self.proc_cmd_send(dict_data)
        except:
            traceback.print_exc()
            
    def handler_recv_data(self):
        sock=self.sock
        while True:
            try:
                recv_data=sock.recv(8092)
                data_str=recv_data.decode('utf-8')
                dict_data=json.loads(data_str)
                self.proc_parse_data(dict_data)
            except:
                traceback.print_exc()
                break
    
    def start(self,addr):
        try:
            sock=socket(AF_INET,SOCK_STREAM)
            sock.connect(addr)
            tcpsock_send_dict_data(sock,{'cmd':'reg'})
            self.sock=sock
            self.transfer_server_addr=addr
            _thread.start_new_thread(self.handler_recv_data,())
        except:
            traceback.print_exc()
    












if __name__ == '__main__':
    print('in')
    # transfer_server_addr=('1.13.3.108',9999)
    transfer_server_addr=('172.16.24.5',9999)
    target_server_address=('172.16.24.5',12345)
    lc=LocalComponent(target_server_address)
    lc.start(transfer_server_addr)
    input()
    print('exit')