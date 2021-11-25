import socketserver
import socket

class MyServer(socketserver.BaseRequestHandler):
    def __init__(self,request,client_address,server):
        self.timeout_s=10
        self.recv_buf_size=8192
        # init过程中会调用setup
        super().__init__(request,client_address,server)
        
    def proc_connected(self):
        print('connected from',self.client_address)
    # 一般接收到零长度数据视为客户端异常断开链接
    def proc_recv_empty_data(self):
        print('empty data from',self.client_address)
    def proc_recv_data(self,data):
        print("recv data from:",self.client_address)
    def proc_except_timeout(self,e):
        print("{} no data timeout({}s), disconnect by server".format(self.client_address,self.timeout_s))
    def proc_except_other(self):
        print("{} disconnected by unknown reason".format(self.client_address))        
        
        
    def handle(self):
        while True:
            try:
                data=self.request.recv(self.recv_buf_size)
                if data==b'':
                    self.proc_recv_empty_data()
                    break
                self.proc_recv_data(data)
            except socket.timeout as e:
                self.proc_except_timeout(e)
                break
            except:
                self.proc_except_other()
                break
                
    def setup(self):
        self.request.settimeout(self.timeout_s)
        self.proc_connected()

if __name__ == '__main__':
    print('>>>')
    s1=socketserver.ThreadingTCPServer(("172.16.24.5",9999),MyServer)
    s1.serve_forever()