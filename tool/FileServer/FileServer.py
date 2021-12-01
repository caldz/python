import socketserver
import socket
import time, sys, threading, logging
import tcp_server_template
logging.basicConfig(format="Time[%(asctime)s] %(threadName)s[%(thread)d]: %(message)s", stream=sys.stdout, level=logging.INFO)

class FileServerHandler(tcp_server_template.ServerHandlerTemplate):
    def __init__(self,request,client_address,server):
        super().set_timeout_s(30)
        super().__init__(request,client_address,server)
    def setup(self):
        super().setup()
        self.file_name = './{}##{}.txt'.format(\
            time.strftime("(%Y-%m-%d_%H-%M-%S)", time.localtime()),
            self.client_address,
        )
        self.file_is_created=False
    def finish(self):
        if self.file_is_created:
            self.file.close()
    def proc_recv_data(self,data):
        if not self.file_is_created:
            self.file = open(self.file_name, mode='wb')
            self.file_is_created=True
        # logging.info("recv data fromss {}".format(self.client_address))
        self.file.write(data)

if __name__ == '__main__':
    server_address=('172.16.24.5',12345)
    tcp_server_template.run_tcp_server(server_address,FileServerHandler)
    print('exit')