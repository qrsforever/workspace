#!/usr/bin/env python

"""
Synopsis:
  Python microservice client.

Usage:
  ./microservice_client.py [OPTIONS]

Options:
  --help               show this help information
  --count              Number of requests to make times 3 (default 10)
  --node               The hostname or node (default crow)

Example:
  $ python microservice_client.py --node=crow --count=20
"""

import json
import itertools
import tornado.ioloop
from tornado import gen
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.options import define, parse_command_line, options


#
# define the command line options.
define(
    "node",
    type=str,
    default="localhost",
    help="The hostname or node",
)
define(
    "count",
    type=int,
    default=10,
    help="Number of requests to make times 3",
)


def show_response(response):
    url = '"{}"'.format(response.request.url)
    url = url.ljust(30)
    length = len(response.body)
    print('url: {}  length: {}'.format(url, length), end='  ')
    content = response.body
    contentjs = json.loads(content.decode())
    print('host_name: "{}"  method: {}  delay: {}'.format(
        contentjs['host_name'],
        contentjs['request_method'],
        contentjs['delay'],
    ))


def make_request(urls, methods):
    print('>>> creating request')
    url = urls.__next__()
    method = methods.__next__()
    body = None if method == 'GET' else ''
    request = HTTPRequest(url, method=method, body=body)
    return request


async def send_request(http_client, request):
    print('<<< sending request')
    response = await http_client.fetch(request)
    return response


async def run():
    http_client = AsyncHTTPClient()
    urls1 = [
        'http://{}:8800/{}'.format('localhost', path) for path in
        ('', 'hello', 'goodbye', )
    ]
    urls2 = itertools.cycle(urls1)
    methods = itertools.cycle(['GET', 'PUT', 'POST'])
    # Create an iterable containing the requests.
    requests = (make_request(urls2, methods) for _ in range(options.count))
    # Send the requests in parallel.
    result = gen.multi([
        send_request(
            http_client,
            request,
        ) for request in requests])
    # Wait until all the requests have been responded to.
    responses = await result
    print('-' * 20)
    print('response count: {}'.format(len(responses)))
    for idx, response in enumerate(responses):
        print('{:>3}.'.format(idx + 1), end=' ')
        show_response(response)


def main():
    parse_command_line()
    io_loop = tornado.ioloop.IOLoop.current()
    io_loop.run_sync(run)


if __name__ == "__main__":
    #import ipdb; ipdb.set_trace()
    main()
