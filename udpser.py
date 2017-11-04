#!/usr/bin/python

from socket import *
from time import ctime

HOST='127.0.0.1'
PORT=60666
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpsersocket = socket(AF_INET, SOCK_DGRAM, 0)
udpsersocket.bind(ADDR)

for i in range(10):
    data, addr = udpsersocket.recvfrom(BUFSIZE)
    print('recv address is:', addr)
    print(data)
    if not data:
        break
    udpsersocket.sendto(('[%s] %s'%(ctime(), data)).encode(), ADDR)
udpsersocket.close()