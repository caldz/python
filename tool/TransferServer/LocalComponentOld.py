from socket import *
import sys,json,base64
import chad,tcp_server_template
import logging,threading,select
import traceback
logging.basicConfig(format="Time[%(asctime)s] %(threadName)s[%(thread)d]: %(message)s", stream=sys.stdout, level=logging.INFO)

class Cmd:
    tag_cmd='cmd'
    class MainClient:
        def reg_ok():
            return {Cmd.tag_cmd:'sm_reg_ok'}
    class SubClient:
        def connect():
            return {Cmd.tag_cmd:'sc_connect'}
        def disconnect():
            return {Cmd.tag_cmd:'sc_disconnect'}
        def send():
            return {Cmd.tag_cmd:'sc_send'}
        def recv():
            return {Cmd.tag_cmd:'sc_recv'}
    
def tcpsock_send_dict_data(tcpsock,dict_data):
    json_str=json.dumps(dict_data)
    tcpsock.send(json_str.encode(encoding='utf-8'))

class LcRoute:
    def __init__(self):
        self.sock=None
        self.real_address=None
def lc_routes_get_lcr_by_addr(lc_routes,addr):
    for lcr in lc_routes:
        if lcr.real_address==addr:
            return lcr
    return None
    
    
def handler_recv_data_from_transer_server(self):
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
            
def handler_recv_data_from_client_of_targer_server(self,lcr):
    sock=lcr.sock
    while True:
        try:
            recv_data=sock.recv(8092)
            if recv_data==b'':
                print('target server has disconnected')
                break
            dict_data=Cmd.SubClient.recv()
            dict_data['base64_data']=str(base64.b64encode(recv_data),encoding='utf-8')
            dict_data['client_address']=lcr.real_address
            print('make dict_data:',dict_data)
            json_str=json.dumps(dict_data)
            self.sock.send(json_str.encode(encoding='utf-8'))
        except ConnectionAbortedError:
            break
        except:
            traceback.print_exc()
            break
            

def handler_recv_data_from_target_server(self,lcr):
    sock=lcr.sock
    while True:
        try:
            recv_data=sock.recv(8092)
            if recv_data==b'':
                print('target server has disconnected')
                break
            dict_data=Cmd.SubClient.recv()
            dict_data['base64_data']=str(base64.b64encode(recv_data),encoding='utf-8')
            dict_data['client_address']=lcr.real_address
            print('make dict_data:',dict_data)
            json_str=json.dumps(dict_data)
            self.sock.send(json_str.encode(encoding='utf-8'))
        except ConnectionAbortedError:
            break
        except:
            traceback.print_exc()
            break

class LocalComponent:
    
    def __init__(self,target_server_address):
        self.lc_routes=set()
        self.transfer_server_addr=None
        self.target_server_addr=target_server_address
    
            
    def proc_cmd_connect(self,dict_data):
        lcr=LcRoute()
        lcr.sock=socket(AF_INET,SOCK_STREAM)
        lcr.sock.connect(self.target_server_addr)
        lcr.real_address=dict_data['client_address']
        self.lc_routes.add(lcr)
        threading.Thread(target=handler_recv_data_from_client_of_targer_server,args=(self,lcr,)).start()
    def proc_cmd_disconnect(self,dict_data):
        lcr=lc_routes_get_lcr_by_addr(self.lc_routes,dict_data['client_address'])
        lcr.sock.close()
        self.lc_routes.remove(lcr)
    def proc_cmd_send(self,dict_data):
        str_base64_data=dict_data['base64_data']
        data=base64.b64decode(str_base64_data)
        lcr=lc_routes_get_lcr_by_addr(self.lc_routes,dict_data['client_address'])
        lcr.sock.send(data)
    def proc_parse_data(self,dict_data):
        print('recv dict_data:',dict_data)
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
        
    
    
    def start(self,addr):
        try:
            sock=socket(AF_INET,SOCK_STREAM)
            sock.connect(addr)
            tcpsock_send_dict_data(sock,{'cmd':'reg'})
            self.sock=sock
            self.transfer_server_addr=addr
            threading.Thread(target=handler_recv_data_from_transer_server,args=(self,)).start()
        except:
            traceback.print_exc()
    











def address_init_by_configure_file():
    tra=chad.Jreader('./server_config.plat.json').search('server_address',\
        empval=('1.13.3.108',9999))
    taa=chad.Jreader('./local_component.plat.json').search('target_server_address',\
        empval=('172.16.24.19',12345))
    print('transfer_server_address=',tra)
    print('target_server_address=',taa)
    return (tra,taa)
if __name__ == '__main__':
    print('in')
    (transfer_server_address,target_server_address)=address_init_by_configure_file()
    lc=LocalComponent(target_server_address)
    lc.start(transfer_server_address)
    while True:
        try:
            input()
            logging.info(threading.enumerate())
        except:
            traceback.print_exc()
    print('exit')