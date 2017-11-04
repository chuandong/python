#!/usr/bin/python

import socketserver 
from time import ctime

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('connect from :', self.client_address)
        self.data = self.request.recv(1024).strip().decode()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper().encode())

print('waiting for connect...')

if __name__ == "__main__":
    HOST, PORT = "localhost", 60006
    with socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()