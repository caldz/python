import logging
import sys
import socketserver
import socket
import threading
from typing import TextIO
import FileOp
import time
from threading import Event

logging.basicConfig(format="%(asctime)s %(thread)d %(threadName)s %(message)s", stream=sys.stdout, level=logging.INFO)


class Handler(socketserver.BaseRequestHandler):

    def setup(self):
        self.event = threading.Event()
        logging.info("新加入了一个连接{}".format(self.client_address))
        file_name = './{}_{}.txt'.format('tag', time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
        self.file = open(file_name, mode='wb')

    def handle(self):
        sk = self.request
        while not self.event.is_set():
            try:
                data = sk.recv(1024)
                if len(data) > 0:
                    self.has_data=True
                    logging.info('recv[{}]:{}'.format(len(data), data))
                    self.file.write(data)
            except Exception as e:
                logging.info(e)
                logging.info('断开链接111')
                sk.close()
                break

        logging.info(data)
        # msg = "{}-{}".format(self.client_address, data).encode()
        # sk.send(msg)
        

    def finish(self):
        logging.info('断开连接')
        self.event.set()
        self.request.close()
        self.file.close()


if __name__ == '__main__':
    server_config = FileOp.get_server_config()
    print(server_config)
    server = socketserver.ThreadingTCPServer((server_config['server_ip'], server_config['server_port']), Handler)
    threading.Thread(target=server.serve_forever, name="server").start()
    while True:
        cmd = input(">>>")
        if cmd.strip() == "quit":
            server.shutdown()
            server.server_close()
            break
        logging.info(threading.enumerate())
    print('exit')
