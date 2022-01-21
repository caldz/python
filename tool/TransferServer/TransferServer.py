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
        self.rest_data=bytes()
        self.set_timeout_s(60*60)
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
            self.request.settimeout(60*60)
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
        # print(self.client_address,': ',data)
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
    def proc_recv_data_from_target(self,new_data):
        try:
            data=self.rest_data+new_data
            if b''!=self.rest_data:
                print('rest data: ',self.rest_data,', new_data:',new_data,', final data: ',data)
            self.rest_data=b''
            data_len=len(data)
            # print(data_len,':',data)
            pack_len_size=4
            cur_i=0
            cur_end=0
            while data_len>cur_end:
                cur_end=cur_i+pack_len_size
                if cur_end > data_len:
                    self.rest_data=data[cur_i:]
                    break
                pack_len_str=str(data[cur_i:cur_end],encoding='utf-8')
                pack_len=int(pack_len_str)
                cur_i=cur_end
                cur_end=cur_i+pack_len
                if cur_end > data_len:
                    self.rest_data=data[cur_i:]
                    break
                dict_data_str=str(data[cur_i:cur_end],encoding='utf-8')
                dict_data=json.loads(dict_data_str)
                if dict_data['cmd']=='sc_recv':
                    parse_data=base64.b64decode(dict_data['base64_data'])
                    client_address=tuple(dict_data['client_address'])
                    client=self.mdl_get_client(client_address)
                    client.request.send(parse_data)
                    # print(parse_data)
                else:
                    print('!!!!BREAK!!!!')
                    break
                cur_i=cur_end
                print('cur_end:',cur_end,', data_len:',data_len, ', rest_data: ', self.rest_data)
        except:
            print(self.client_address,': ',data)
            perr('##ERROR##')
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
    
    
