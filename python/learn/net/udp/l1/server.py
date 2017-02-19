#!/usr/bin/env python

from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print ('wait for client ...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    if not data:
        break
    udpSerSock.sendto('[%s]: %s' % (ctime(), data), addr)

udpSerSock.close()
