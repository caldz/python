import socketserver
import socket
import time, sys, threading, logging, tcp_server_template
logging.basicConfig(format="Time[%(asctime)s] %(threadName)s[%(thread)d]: %(message)s", stream=sys.stdout, level=logging.INFO)

class FileServerHandler(tcp_server_template.ServerHandlerTemplate):
    def __init__(self,request,client_address,server):
        h=super()
        h.set_timeout_s(5)
        h.__init__(request,client_address,server)
    def proc_recv_data(self,data):
        # logging.info("recv data fromss {}".format(self.client_address))
        pass

if __name__ == '__main__':
    server_ip='172.16.24.5'
    server_port=9999
    tcp_server_template.run_server(server_ip,server_port,FileServerHandler)
    print('exit')