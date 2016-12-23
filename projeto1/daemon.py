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

    s.listen(1)
    while True:

        conn, addr = s.accept()
        print 'Connection address: ', addr

        try:
            serialialized_header = conn.recv(1024)
            if not serialialized_header: break

            header = Header(serialialized_header)

            header = Header(serialialized_header)
            cksum_received = header.checksum
            header.checksum = 0
            cksum_new = header.cksum(header.serialToList(header.make_header()))
            if (cksum_received != cksum_new):
                print 'erro no checksum'
                break
            else:
                header.checksum = cksum_new

            if header.protocol == 1:
                args = header.options.replace('|', '').replace(';', '').replace('>', '')

                print 'args', args
                out = subprocess.check_output(["ps", args])

                print 'out', out

                print >> sys.stderr, 'sending data back out to the client'
                s.sendall(out)
                print 'enviou e recebeu'
            '''
            if header.protocol == 2:
                args = header.options.replace('|', '').replace(';', '').replace('>', '')

                print 'args', args
                out = subprocess.check_output(["df", args])

                print 'out',out
                print >> sys.stderr, 'sending data back out to the client'
                s.sendall(out)

            if header.protocol == 3:
                args = header.options.replace('|', '').replace(';', '').replace('>', '')

                print 'args', args
                out = subprocess.check_output(["df", args])

                print 'out',out
                print >> sys.stderr, 'sending data back out to the client'
                s.sendall(out)

            if header.protocol == 4:
                args = header.options.replace('|', '').replace(';', '').replace('>', '')

                print 'args', args
                out = subprocess.check_output(["uptime", args])

                print 'out',out

                print >> sys.stderr, 'sending data back out to the client'
                s.sendall(out)

            '''
            print 'Received data: ', serialialized_header

        finally:
            conn.close()


        break