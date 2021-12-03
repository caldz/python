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


class Client:
    def __init__(self):
        self.addr
        self.sock

class TranferServerHandler(tcp_server_template.ServerHandlerTemplate):
    class MyData:
        sm_stat='wait_reg'
        handler=None
        client_list=set()
    reg_socket_data=MyData()
    
    # 简化函数-数据
    def mdt(self):
        return TranferServerHandler.reg_socket_data.handler.request
    def mda(self):
        return TranferServerHandler.reg_socket_data.handler.client_address
    def mds(self):
        return TranferServerHandler.reg_socket_data.sm_stat
    def mdl(self):
        return TranferServerHandler.reg_socket_data.client_list
    def set_mds(self,stat):
        TranferServerHandler.reg_socket_data.sm_stat=stat
    def set_mdta(self,handler):
        TranferServerHandler.reg_socket_data.handler=handler

    # 简化函数-函数
    def mdl_get_client(self,client_address):
        for client in self.mdl():
            print(client_address, client.client_address)
            if client_address==client.client_address:
                return client
        return None
        
    def send_tcp_data_by_dict(self,dict_data):
        dict_data['client_address']=self.client_address
        json_str=json.dumps(dict_data)
        self.mdt().send(json_str.encode(encoding='utf-8'))
        
    # 调试函数-函数
    def print_mdl(self):
        pass
        # print('---------mdl({})-----------'.format(len(self.mdl())))
        # for a in self.mdl():
            # print(a)

    def __init__(self,request,client_address,server):
        self.set_timeout_s(60)
        self.clients=set()
        super().__init__(request,client_address,server)
        
    def setup(self):
        super().setup() 
        if self.mds()=='transfer':
            try:
                self.send_tcp_data_by_dict(Cmd.SubClient.connect())
                self.mdl().add(self)
                self.print_mdl()
            except:
                perr('disconnect')
    
    def proc_wait_reg(self,tcp_data):
        try:
            dict_data=json.loads(str(tcp_data,encoding='utf-8'))
            self.set_mdta(self)
            self.set_mds('transfer')
            self.send_tcp_data_by_dict(Cmd.MainClient.reg_ok())
            self.request.settimeout(600)
            print('Start Transfer---------------')
        except:
            perr('err reg data from {}'.format(self.client_address))
            self.request.send('Invalid Data'.encode(encoding='utf-8'))
            self.request.close()
            
    def proc_transfer(self,data):
        print(self.client_address,self.mda())
        if self in self.mdl():
            self.proc_sub_client_send_data(data)
        elif self.client_address==self.mda():
            self.proc_main_client_send_data(data)
        
    def proc_recv_data(self,data):
        if self.mds()=='wait_reg':
            self.proc_wait_reg(data)
        elif self.mds()=='transfer':
            self.proc_transfer(data)
    
    def finish(self):
        super().finish() 
        if self.mds()=='transfer':
            if self.client_address==self.mda():
                self.proc_main_client_disconnect()
                self.proc_sub_client_disconnect()
    
    def proc_sub_client_send_data(self,data):
        try:
            dict_data=Cmd.SubClient.send()
            dict_data['base64_data']=str(base64.b64encode(data),encoding='utf-8')
            self.send_tcp_data_by_dict(dict_data)
        except:
            perr('')
    def proc_main_client_send_data(self,data):
        try:
            dict_data=json.loads(str(data,encoding='utf-8'))
            if dict_data['cmd']=='sc_recv':
                data=base64.b64decode(dict_data['base64_data'])
                client_address=tuple(dict_data['client_address'])
                client=self.mdl_get_client(client_address)
                client.request.send(data)
        except:
            perr('')
    def proc_main_client_disconnect(self):
        self.mdl().clear()
        self.set_mds('wait_reg')
        print('Finish Transfer=============')
        
    def proc_sub_client_disconnect(self):
        self.send_tcp_data_by_dict(Cmd.SubClient.disconnect())
        self.mdl().remove(self)
        self.print_mdl()
            


if __name__ == '__main__':
    addr=chad.Jreader('./server_config.plat.json').search('server_address',empval=('192.168.0.102',9999))
    print('addr=',addr)
    tcp_server_template.run_tcp_server(addr,TranferServerHandler)
    print('exit')
    input()
    
    
