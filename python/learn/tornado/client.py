#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import websocket
import logging
import time
import requests
import threading
from tornado import gen
from tornado.httpclient import AsyncHTTPClient, HTTPRequest

def handle_request(response):
    logging.info("handle_request")

def run_socket(*args):
    logging.info("run_socket")
    global sess
    sess = requests.Session()
    resp = sess.post(sock_addr, json='{}')
    print('{}'.format(resp))

    time.sleep(3) 

def main():
    parser = argparse.ArgumentParser(description='Start the process monitor server.')
    parser.add_argument('-port', metavar='port', type=int,
                        default=8184,
                        help='port to run the server on.')
    parser.add_argument('-loglevel', metavar='loglevel',
                        default='INFO',
                        help='log level (default = INFO)')
    options = parser.parse_args()
    logging.getLogger().setLevel(options.loglevel)
    global sock_addr
    sock_addr = "http://localhost:{}/process_request".format(options.port)
    logging.info(sock_addr)
    socket_thread = threading.Thread(
        target=run_socket,
        name='Socket-Thread'
        )
    socket_thread.start()
    time.sleep(2)
    # sock_addr = "ws://localhost:{}/process_socket".format(options.port)
    # ws = websocket.WebSocketApp(sock_addr)
    # ws.run_forever(ping_interval=0)

if __name__ == "__main__":
    main()
    # sess.close()
    time.sleep(10) 
