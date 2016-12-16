#!/usr/bin/env python
import socket
import sys

if len(sys.argv) < 3:
    print 'Erro: argumento faltante. ex: --port 9001'
else:

    porta = int(sys.argv[2])
    ip = '127.0.0.1'
    buffer_size = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip,porta))

    while True:
        s.listen(1)
        conn, addr = s.accept()
        print 'Connection address: ', addr

        while True:
            data = conn.recv(buffer_size)
            if not data: break
            print 'Received data: ', data

        conn.close()
        break