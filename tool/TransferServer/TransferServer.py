import socketserver
from socket import socket
from socket import *
import time, sys, threading, logging, json, traceback
import base64

import chad,tcp_server_template

logging.basicConfig(format="Time[%(asctime)s] %(threadName)s[%(thread)d]: %(message)s", stream=sys.stdout, level=logging.INFO)

def perr(tag):
    traceback.print_exc()
    # print('{}, Unexpected Error:{}'.format(tag,sys.exc_info()))


# 协议处理模块
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

# 连接管理模块
class ClientConnectionMgr:
    def __init__(self):
        self.main_connection=None
        self.state='wait_reg'
        self.sub_connection_s=set()
    def get_main_connection(self):
        return self.main_connection
    def get_sub_connection_s(self)->set:
        return self.sub_connection_s
    def get_state(self)->str:
        return self.state
    def set_main_connection(self,main_connection):
        self.main_connection=main_connection
    def set_state(self,state:str):
        self.state=state
ccm=ClientConnectionMgr()

class TranferServerHandler(tcp_server_template.ServerHandlerTemplate):
    # 简化函数-函数
    def mdl_get_client(self,client_address):
        for client in ccm.get_sub_connection_s():
            # print(client_address, client.client_address)
            if client_address==client.client_address:
                return client
        return None
        
    def send_tcp_data_by_dict(self,dict_data):
        dict_data['client_address']=self.client_address
        json_str=json.dumps(dict_data)
        ccm.get_main_connection().request.send(json_str.encode(encoding='utf-8'))

    def __init__(self,request,client_address,server):
        self.set_timeout_s(60)
        self.clients=set()
        super().__init__(request,client_address,server)
        
    def setup(self):
        super().setup() 
        if ccm.get_state()=='transfer':
            try:
                self.send_tcp_data_by_dict(Cmd.SubClient.connect())
                ccm.get_sub_connection_s().add(self)
            except:
                perr('disconnect')
    
    def proc_wait_reg(self,tcp_data):
        try:
            dict_data=json.loads(str(tcp_data,encoding='utf-8'))
            ccm.set_main_connection(self)
            ccm.set_state('transfer')
            self.send_tcp_data_by_dict(Cmd.MainClient.reg_ok())
            self.request.settimeout(600)
            print('Start Transfer---------------')
        except:
            perr('err reg data from {}'.format(self.client_address))
            self.request.send('Invalid Data'.encode(encoding='utf-8'))
            self.request.close()
            
    def proc_transfer(self,data):
        try:
            if self in ccm.get_sub_connection_s():
                self.proc_recv_data_from_clients(data)
            elif self.client_address==ccm.get_main_connection().client_address:
                self.proc_recv_data_from_target(data)
        except:
            perr('')
        
    def proc_recv_data(self,data):
        if ccm.get_state()=='wait_reg':
            self.proc_wait_reg(data)
        elif ccm.get_state()=='transfer':
            self.proc_transfer(data)
    
    def finish(self):
        super().finish() 
        if ccm.get_state()=='transfer':
            if self.client_address==ccm.get_main_connection().client_address:
                self.proc_disconnect_from_from_target()
            elif self in ccm.get_sub_connection_s():
                self.proc_disconnect_from_from_clients()
    
    def proc_recv_data_from_clients(self,data):
        try:
            dict_data=Cmd.SubClient.send()
            dict_data['base64_data']=str(base64.b64encode(data),encoding='utf-8')
            self.send_tcp_data_by_dict(dict_data)
        except:
            perr('')
    def proc_recv_data_from_target(self,data):
        try:
            # print('recv data',data)
            dict_data=json.loads(str(data,encoding='utf-8'))
            if dict_data['cmd']=='sc_recv':
                data=base64.b64decode(dict_data['base64_data'])
                client_address=tuple(dict_data['client_address'])
                client=self.mdl_get_client(client_address)
                client.request.send(data)
        except:
            perr('')
    def proc_disconnect_from_from_target(self):
        ccm.get_sub_connection_s().clear()
        ccm.set_state('wait_reg')
        print('Finish Transfer=============')
        
    def proc_disconnect_from_from_clients(self):
        self.send_tcp_data_by_dict(Cmd.SubClient.disconnect())
        ccm.get_sub_connection_s().remove(self)
            


if __name__ == '__main__':
    addr=chad.Jreader('./server_config.plat.json').search('server_address',empval=('192.168.0.102',9999))
    print('addr=',addr)
    tcp_server_template.run_tcp_server(addr,TranferServerHandler)
    print('exit')
    input()
    
    
