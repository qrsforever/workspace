#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import time

class TCPClient(object):

    def __init__(self, bufsize):
        self.connectted = False
        self.buf_size = bufsize

    def connect(self, srv_addr, srv_port):
        self.srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srv_socket.connect((srv_addr, int(srv_port))) 
        result = self.srv_socket.recv(8).decode('utf-8')
        if result != 'success':
            return False
        self.connectted = True
        return True

    def close(self):
        if self.connectted:
            self.srv_socket.send(b'quit')
            time.sleep(0.3)
            self.srv_socket.close()

    def command(self, cmd, *args):
        if not self.connectted:
            return None

        cmdstr = cmd;
        for arg in args:
            cmdstr += ';'
            cmdstr += arg

        self.srv_socket.send(cmdstr.encode())
        return self.srv_socket.recv(self.buf_size).decode('utf-8')
