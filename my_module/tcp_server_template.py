import socketserver
import socket
import time, sys, threading, logging
logging.basicConfig(format="Time[%(asctime)s] %(threadName)s[%(thread)d]: %(message)s", stream=sys.stdout, level=logging.INFO)


def run_server(server_ip, server_port,handler):
    logging.info('start server>>>')
    server=socketserver.ThreadingTCPServer((server_ip,server_port),handler)
    threading.Thread(target=server.serve_forever, name="server").start()
    while True:
        cmd = input('')
        # if cmd.strip() == "quit":
            # server.shutdown()
            # server.server_close()
            # break
        logging.info(threading.enumerate())
    
class ServerHandlerTemplate(socketserver.BaseRequestHandler):
    timeout_s=10
    recv_buf_size=8192
    def set_timeout_s(self,timeout_s):
        self.timeout_s=timeout_s
    def set_recv_buf_size(self,recv_buf_size):
        self.recv_buf_size=recv_buf_size
    def __init__(self,request,client_address,server):
        # init过程中会调用setup
        super().__init__(request,client_address,server)
        
    def proc_connected(self):
        logging.info('connect from {}, accept'.format(self.client_address))
    # 一般接收到零长度数据视为客户端异常断开链接
    def proc_recv_empty_data(self):
        logging.info('empty data from {}, disconnect'.format(self.client_address))
    def proc_recv_data(self,data):
        logging.info("recv data from {}".format(self.client_address))
    def proc_except_timeout(self,e):
        logging.info("no data timeout({}s) from {}, disconnect".format(self.timeout_s,self.client_address))
    def proc_except_other(self):
        logging.info("unknown error from {}, disconnect".format(self.client_address))        
        
        
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
    server_ip='172.16.24.5'
    server_port=9999
    run_server(server_ip,server_port,ServerHandlerTemplate)
    print('exit')