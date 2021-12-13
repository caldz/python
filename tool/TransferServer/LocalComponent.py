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

class LocalComponent:
    
    def __init__(self,target_server_address):
        self.scm=SocketClientManager(target_server_address)
        self.transfer_server_addr=None
        self.working_flag=False
    
    def is_exit(self):
        return Ture
    
    def start(self,addr):
        self.working_flag=True
        try:
            sock=socket(AF_INET,SOCK_STREAM)
            sock.connect(addr)
            tcpsock_send_dict_data(sock,{'cmd':'reg'})
            self.transfer_sock=sock
            self.transfer_server_addr=addr
            threading.Thread(target=self.run,args=()).start()
        except:
            self.working_flag=False
            traceback.print_exc()
        return self
 
    def run(self):
        timeout=10
        transfer_sock=self.transfer_sock
        inputs=[transfer_sock,]
        working_flag=True
        while working_flag:
            try:
                read_list,write_list,error_list=select.select(inputs,[],inputs,timeout)
                print(read_list, error_list)
                for r in read_list:
                    recv_data=r.recv(8092)
                    if recv_data==b'':
                        inputs.remove(r)
                        working_flag=False
                        if r==transfer_sock:
                            print('disconnect from transfer server')
                        else:
                            print('disconnect from target server')
                        break
                    elif transfer_sock==r:
                        # 当收到来自转发服务器的数据时
                        scm=self.scm
                        data_str=recv_data.decode('utf-8')
                        dict_data=json.loads(data_str)
                        print('recv dict_data:',dict_data)
                        cmd=dict_data['cmd']
                        client_address=dict_data['client_address']
                        if cmd=='sc_connect':
                            client_sock=scm.create_client_sock(client_address)
                            inputs.append(client_sock)
                        elif cmd=='sc_disconnect':
                            client_sock=scm.free_client_sock(client_address)
                            inputs.remove(client_sock)
                        elif cmd=='sc_send':
                            str_base64_data=dict_data['base64_data']
                            send_data=base64.b64decode(str_base64_data)
                            scm.send_to_client_sock(client_address,send_data)
                    else:
                        # 当收到来自目标服务器的数据时
                        dict_data=Cmd.SubClient.recv()
                        dict_data['base64_data']=str(base64.b64encode(recv_data),encoding='utf-8')
                        dict_data['client_address']=scm.get_client_address_by_client_sock(r)
                        print('make dict_data:',dict_data)
                        tcpsock_send_dict_data(transfer_sock,dict_data)
            except:
                traceback.print_exc()
                break
        # 回收所有资源
        for sock in inputs:
            sock.close()
        self.working_flag=False
        print('Component Finish')

        
    def proc_cmd_disconnect(self,dict_data):
        lcr=lc_routes_get_lcr_by_addr(self.lc_routes,dict_data['client_address'])
        lcr.sock.close()
        self.lc_routes.remove(lcr)
        
    
class SocketClientManager:
    def __init__(self,target_server_address):
        self.target_server_address=target_server_address
        self.sock_dict={}


    def create_client_sock(self,client_address):
        client_sock=socket(AF_INET,SOCK_STREAM)
        client_sock.connect(self.target_server_address)
        self.sock_dict[str(client_address)]=client_sock
        return client_sock
        
        
    def free_client_sock(self,client_address):
        client_sock=self.sock_dict[str(client_address)]
        client_sock.close()
        del(self.sock_dict[str(client_address)])
        return client_sock


    def send_to_client_sock(self,client_address,send_data):
        client_sock=self.sock_dict[str(client_address)]
        client_sock.send(send_data)
        
    def get_client_address_by_client_sock(self,client_sock):
        for key in self.sock_dict.keys():
            if self.sock_dict[key]==client_sock:
                return eval(key)
        return None


def tcpsock_send_dict_data(tcpsock,dict_data):
    json_str=json.dumps(dict_data)
    tcpsock.send(json_str.encode(encoding='utf-8'))













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
    lc=LocalComponent(target_server_address).start(transfer_server_address)
    while lc.is_working():
        try:
            input()
            logging.info(threading.enumerate())
        except:
            traceback.print_exc()
    print('exit')