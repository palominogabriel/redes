#!/usr/bin/env python
import socket
import sys
import subprocess
from header import Header
if len(sys.argv) < 3:
    print 'Erro: argumento faltante. ex: --port 9001'
else:

    porta = int(sys.argv[2])
    ip = '127.0.0.1'
    buffer_size = 10024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip,porta))
    s.timeout(15.0)

    while True:
        s.listen(3)
        conn, addr = s.accept()
        print 'Connection address: ', addr

        while True:
            serialialized_header = conn.recv(buffer_size)
            if not serialialized_header: break

            header = Header(serialialized_header)
            if header.protocol == 1:
                args = header.options.replace('|', '').replace(';', '').replace('>', '')

                print 'args', args
                out = subprocess.check_output(["ps", args])

                print 'out',out
                s.sendall(out)

            if header.protocol == 2:
                args = header.options.replace('|', '').replace(';', '').replace('>', '')

                print 'args', args
                out = subprocess.check_output(["df", args])

                print 'out',out
                s.sendall(out)

            if header.protocol == 3:
                args = header.options.replace('|', '').replace(';', '').replace('>', '')

                print 'args', args
                out = subprocess.check_output(["df", args])

                print 'out',out
                s.sendall(out)

            if header.protocol == 4:
                args = header.options.replace('|', '').replace(';', '').replace('>', '')

                print 'args', args
                out = subprocess.check_output(["uptime", args])

                print 'out',out
                s.sendall(out)


            print 'Received data: ', serialialized_header


        #conn.close()
        break