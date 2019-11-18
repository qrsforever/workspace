#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import tornado.ioloop
import tornado.web
import tornado.websocket 
import logging
import tornado.gen

class ProcessRequestHandler(tornado.web.RequestHandler):
    def initialize(self):
        logging.info('initialize')

    @tornado.gen.coroutine
    def get(self):
        logging.info('get')
        self.write("get")
        self.flush()

    @tornado.gen.coroutine
    def post(self):
        logging.info('post')
        self.write("post")
        self.flush()

    def on_connection_close(self):
        print("#######")
        logging.info('on_connection_close')

class ProcessSocketHandler(tornado.websocket.WebSocketHandler):
    def initialize(self):
        logging.info('initialize')

    def open(self):
        logging.info('open')

    def on_message(self, message):
        logging.info('on_message')

    def on_close(self):
        logging.info('on_close')

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
    routes = [
        (r"/process_socket", ProcessSocketHandler, None),
        (r"/process_request", ProcessRequestHandler, None),
    ]
    logging.info("listen: {}".format(options.port))
    application = tornado.web.Application(routes)
    # application.listen(options.port)
    # tornado.ioloop.IOLoop.current().start()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
