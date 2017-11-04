#!/usr/bin/python

from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 60536
ADDR = (HOST, PORT)
BUFSIZE = 1024

tcpclisocket = socket(AF_INET, SOCK_STREAM, 0)
tcpclisocket.connect(ADDR)

while True:
    data = input('>:')

    if not data:
	    break
    tcpclisocket.send(data.encode())
    data = tcpclisocket.recv(BUFSIZE).decode()
    print(data)
tcpclisocket.close()
