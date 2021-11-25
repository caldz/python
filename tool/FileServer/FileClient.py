import socket
from socket import socket

import FileOp
from socket import *


def read_file_lines(file_path):
    f = open(file_path, 'rb')
    data_list = []
    while True:
        data = f.read(512)
        data_list.append(data)
        print(data)
        if len(data) == 0:
            break
    f.close()
    return data_list


class UploadClient:
    def __init__(self):
        pass

    def set_addr(self, server_ip, server_port):
        self.addr = (server_ip, server_port)
        return self

    def upload_file(self, file_path):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect(self.addr)
        data_list = read_file_lines(file_path)
        for data in data_list:
            sock.send(data)
        sock.close()
        pass


if __name__ == '__main__':
    target_file = './test_log.txt'
    sc = FileOp.get_server_config()
    UploadClient().set_addr(sc['server_ip'], sc['server_port']).upload_file(target_file)
