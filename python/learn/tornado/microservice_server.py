#!/usr/bin/env python

"""
synopsis:
  Python HTTP microservice server.

Usage:
  ./microservice_server.py [OPTIONS]

Options:
  --help               show this help information
  --delay              seconds to delay before responding (default 0.0)
  --goodbyemessage     message for response to '/goodbye' (default goodbye
                       world)
  --hellomessage       message for response to '/hello' (default hello world)
  --message            message for response to '/' (default no one is home)
  --name               name for server (default my_server)
  --port               run on the given port (default 8888)

Example:
  #!/bin/bash -x
  ./microservice_server.py \
      --port=8800 \
      --message=one \
      --hellomessage=two \
      --goodbyemessage=three \
      --name=dave \
      --delay=$1
"""

import requests
import tornado.ioloop
import tornado.web
from tornado.options import define, parse_command_line, options


#
# define the command line options.
define(
    "port",
    default=8800,
    help="run on the given port",
    type=int)
define(
    "message",
    default="no one is home",
    help="message for response to '/'",
    type=str)
define(
    "hellomessage",
    default="hello world",
    help="message for response to '/hello'",
    type=str)
define(
    "goodbyemessage",
    default="goodbye world",
    help="message for response to '/goodbye'",
    type=str)
define(
    "name",
    default="my_server",
    help="name for server",
    type=str)
define(
    "delay",
    default=0.0,
    help="seconds to delay before responding",
    type=float)


class MainHandler(tornado.web.RequestHandler):
    """A Tornado HTTP request handler"""

    def initialize(self, name, msg, delay):
        """Initialize the request.  Called for each request."""
        self.name = name
        self.msg = msg
        self.delay = delay
        self.host_name = requests.utils.socket.gethostname()

    async def get(self):
        """Respond to a GET request."""
        if self.delay > 0.0:
            print('delaying: {}'.format(self.delay))
            await tornado.gen.sleep(self.delay)
        # the set_header to set content-type for json is not needed
        # if we send a dict to the write method
        #self.set_header("content-type", "application/json; charset=utf-8")
        content = {
            'name': self.name,
            'message': self.msg,
            'host_name': self.host_name,
            'request_method': self.request.method,
            'delay': self.delay,
        }
        self.write(content)

    async def put(self):
        """Respond to a PUT request."""
        if self.delay > 0.0:
            print('delaying: {}'.format(self.delay))
            await tornado.gen.sleep(self.delay)
        # the set_header to set content-type for json is not needed
        # if we send a dict to the write method
        #self.set_header("content-type", "application/json; charset=utf-8")
        content = {
            'name': self.name,
            'message': self.msg,
            'host_name': self.host_name,
            'request_method': self.request.method,
            'delay': self.delay,
        }
        self.write(content)

    async def post(self):
        """Respond to a POST request."""
        if self.delay > 0.0:
            print('delaying: {}'.format(self.delay))
            await tornado.gen.sleep(self.delay)
        # the set_header to set content-type for json is not needed
        # if we send a dict to the write method
        #self.set_header("content-type", "application/json; charset=utf-8")
        content = {
            'name': self.name,
            'message': self.msg,
            'host_name': self.host_name,
            'request_method': self.request.method,
            'delay': self.delay,
        }
        self.write(content)

    def on_connection_close(self):
        print("##########close############")


def main():
    parse_command_line()
    routes = [
        (r"/", MainHandler, dict(
            name=options.name,
            msg=options.message,
            delay=options.delay,
        )),
        (r"/hello", MainHandler, dict(
            name=options.name,
            msg=options.hellomessage,
            delay=options.delay,
        )),
        (r"/goodbye", MainHandler, dict(
            name=options.name,
            msg=options.goodbyemessage,
            delay=options.delay,
        )),
    ]
    application = tornado.web.Application(routes)
    # application.listen(options.port)
    # tornado.ioloop.IOLoop.current().start()

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    #import ipdb; ipdb.set_trace()
    main()
