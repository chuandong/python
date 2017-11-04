#!/usr/bin/python

from socket import *

HOST = '127.0.0.1'
PORT = 60006
ADDR=(HOST, PORT)
BUFSIZE = 1024

while True:
    socktcpcli = socket(AF_INET, SOCK_STREAM, 0)
    socktcpcli.connect(ADDR)
    data = input('>:')
    if not data:
        break
    socktcpcli.send(('%s\t\n'%data).encode())
    data = socktcpcli.recv(BUFSIZE).decode()
    if not data:
        break
    print(data)
    
socktcpcli.close()