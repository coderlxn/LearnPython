# -*- coding: utf-8 -*-
# @Time    : 9/28/18 7:35 PM
# @Author  : Jax.Li
# @FileName: httpfileserver.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import os
import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer


def start_http_file_server(plugin_dir, port):
    print("start http file server")

    handler_class = SimpleHTTPRequestHandler
    protocol = 'HTTP/1.0'
    server_address = ('0.0.0.0', port)
    SimpleHTTPRequestHandler.protocol_version = protocol
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    if os.path.isdir(plugin_dir):
        os.chdir(plugin_dir)
    else:
        print('no such dir: %s' % plugin_dir)
        sys.exit()

    sa = httpd.socket.getsockname()
    print('Serving HTTP on %s:%s' % (sa[0], sa[1]))

    httpd.serve_forever()


if __name__ == '__main__':
    start_http_file_server(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugins'), 8080)