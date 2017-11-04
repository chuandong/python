#!/usr/bin/python

from socket import *
from time import ctime

HOST='127.0.0.1'
PORT=60666
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpclisocket = socket(AF_INET, SOCK_DGRAM, 0)

while True:
    data = input('>:')
    if not data:
        break
    udpclisocket.sendto(((data).encode()), ADDR)
    
    
    data = udpclisocket.recvfrom(BUFSIZE).decode()
    if not data:
        break
    print(data)
udpclisocket.close()