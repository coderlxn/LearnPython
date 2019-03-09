# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 4:54 PM
# @Author  : Jax.Li
# @FileName: server.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import socket
import selectors
import types


sel = selectors.DefaultSelector()

HOST = "127.0.0.1"
PORT = 65432

l_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
l_sock.bind((HOST, PORT))
l_sock.listen()
print('listening on', (HOST, PORT))
l_sock.setblocking(False)
sel.register(l_sock, selectors.EVENT_READ, data=None)


def accept_wrapper(sock):
    conn, addr = sock.accept()
    print('accept connection from ', addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data.outb += recv_data
        else:
            print("closing connection to", data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print("echoing", repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]


while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data is None:
            accept_wrapper(key.fileobj)
        else:
            service_connection(key, mask)

