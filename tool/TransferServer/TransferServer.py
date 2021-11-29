import socketserver
from socket import socket
from socket import *
import time, sys, threading, logging, json
import tcp_server_template
logging.basicConfig(format="Time[%(asctime)s] %(threadName)s[%(thread)d]: %(message)s", stream=sys.stdout, level=logging.INFO)

def perr(tag):
    print('{}, Unexpected Error:{}'.format(tag,sys.exc_info()[0]))

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
    def send_tcp_data_by_dict(self,dict_data):
        dict_data['client_address']=self.client_address
        json_str=json.dumps(dict_data)
        self.mdt().send(json_str.encode(encoding='utf-8'))
    
    # def clear_all_reg_socket(self):
        # for reg_socket in self.mdt():
            # reg_socket.request.close()
        # for reg_socket in self.mdl():
            
        
        
    # 调试函数-函数
    def print_mdl(self):
        print('---------mdl-----------')
        for a in self.mdl():
            print(a)
        print('=========mdl===========')

    def __init__(self,request,client_address,server):
        self.set_timeout_s(10)
        super().__init__(request,client_address,server)
        
    def setup(self):
        super().setup() 
        if self.mds()=='transfer':
            try:
                self.send_tcp_data_by_dict({'cmd':'ts_info','result':'connnect'})
                self.mdl().add(self)
                self.print_mdl()
            except:
                perr('disconnect')
    
    def finish(self):
        super().finish() 
        if self.mds()=='transfer':
            try:
                if self.client_address==self.mda():
                    self.mdl().clear()
                    self.set_mds('wait_reg')
                    print('Finish Transfer=============')
                elif self in self.mdl():
                    self.send_tcp_data_by_dict({'cmd':'ts_info','result':'disconnect'})
                    self.mdl().remove(self)
                    self.print_mdl()
                else:
                    pass
            except:
                perr('disconnect')
            
    def proc_main(self,data):
        if self.mds()=='wait_reg':
            self.proc_wait_reg(data)
        elif self.mds()=='transfer':
            self.proc_transfer(data)
            
    def proc_wait_reg(self,tcp_data):
        try:
            dict_data=json.loads(str(tcp_data,encoding='utf-8'))
            self.set_mdta(self)
            self.set_mds('transfer')
            self.send_tcp_data_by_dict({'cmd':'resp','result':'ok'})
            self.request.settimeout(600)
            print('Start Transfer---------------')
        except:
            perr('err reg data from {}'.format(self.client_address))
            self.request.send('Invalid Data'.encode(encoding='utf-8'))
            self.request.close()
            
    def proc_transfer(self,data):
        try:
            if self in self.mdl():
                self.send_tcp_data_by_dict({'cmd':'ts_info','result':'send'})
        except:
            perr('')
        
    def proc_recv_data(self,data):
        self.proc_main(data)

if __name__ == '__main__':
    server_ip='172.16.24.5'
    server_port=9999
    tcp_server_template.run_server(server_ip,server_port,TranferServerHandler)
    print('exit')