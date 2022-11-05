import socket
import time

import network

s = socket.socket()         # 创建 socket 对象
host = '192.168.31.25'     # esp32 ip
port = 10000                # 设置端口号

s.connect((host, port))

if __name__ == '__main__':
    while True:
        i=1
        msg = 'helloworld'+i
        data=msg.encode()
        s.send(data)
        time.sleep(1)
        i=i+1