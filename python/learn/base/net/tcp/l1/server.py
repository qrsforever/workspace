#!/usr/bin//env python

from socket import *
from time import ctime

HOST = ''
PORT = 21467
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('wait client...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('connect from:', addr)
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data :
            break
        tcpCliSock.send('[%s]: %s' % (ctime(), data))
    tcpCliSock.close()

tcpSerSock.close()
