import logging
import sys
import socketserver
import socket
import threading
import time
from threading import Event

logging.basicConfig(format="%(asctime)s %(thread)d %(threadName)s %(message)s", stream=sys.stdout, level=logging.INFO)

class Handler(socketserver.BaseRequestHandler):
    
    def setup(self):
        self.event = threading.Event()
        logging.info("新加入了一个连接{}".format(self.client_address))

    def handle(self):
        sk: socket.socket = self.request
        while not self.event.is_set():
            try:
                data = sk.recv(1024)
                if len(data) > 0:
                    print('recv[{}]:{}'.format(len(data), data))
            except Exception as e:
                logging.info('hehe')
                logging.info(e)
            break
        logging.info(data)
        # msg = "{}-{}".format(self.client_address, data).encode()
        # sk.send(msg)

    def finish(self):
        print('断开连接')
        self.event.set()
        self.request.close()


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('172.16.24.5',22222), Handler)
    threading.Thread(target=server.serve_forever, name="server").start()
    
    while True:
        cmd = input(">>>")
        if cmd.strip() == "quit":
            server.shutdown()
            server.server_close()
            break
        logging.info(threading.enumerate())
    print('exit')
    
    