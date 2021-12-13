from socket import *
import traceback,logging,sys,select
logging.basicConfig(format="Time[%(asctime)s] %(threadName)s[%(thread)d]: %(message)s", stream=sys.stdout, level=logging.INFO)


class MyTcpSrv:
    def __init__(self,addr):
        self.addr=addr
        self.sock_dict={}
        self.wait_timeout_s=10
        pass
        
        
    def start(self):
        srv_address=self.addr
        
        srv_sock=socket(AF_INET,SOCK_STREAM)
        # srv_sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        srv_sock.bind(srv_address)
        srv_sock.listen(10)
        # srv_sock.setblocking(False)
        self.sock_dict[srv_sock.fileno()]=srv_sock
        
        self.srv_sock=srv_sock
        return self
    
    def run(self):
        timeout=self.wait_timeout_s
        srv_sock=self.srv_sock
        inputs=[srv_sock,]
        while True:
            read_list,write_list,error_list=select.select(inputs,[],inputs,timeout)
            print(read_list, write_list, error_list)
            for r in read_list:
                if srv_sock==r:
                    request,address=r.accept()
                    inputs.append(request)
                else:
                    recv_data=r.recv(1024)
                    if recv_data:
                        print('recv_data', recv_data)
                    else:
                        inputs.remove(r)

if __name__=='__main__':
    logging.info('in')
    addr=('172.16.24.19',22222)
    ts=MyTcpSrv(addr).start()
    ts.run()
    logging.info('exit')
    input()