#!/usr/bin/python

from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 60536
ADDR = (HOST, PORT)
BUFSIZE = 1024

sersocket = socket(AF_INET, SOCK_STREAM, 0)
sersocket.bind(ADDR)
sersocket.listen(5)

while True:
    print('waiting connection ...', ADDR)
    tcpclisocket, addr = sersocket.accept()
    while True:
        data = tcpclisocket.recv(BUFSIZE).decode()
        if not data:
	        break
        tcpclisocket.send(('[%s] %s' %(ctime(), data)).encode())
        print(data)
    tcpclisocket.close()
sersocket.close()
