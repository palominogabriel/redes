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
    buffer_size = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip,porta))

    while True:
        s.listen(1)
        conn, addr = s.accept()
        print 'Connection address: ', addr

        while True:
            serialialized_header = conn.recv(buffer_size)
            if not serialialized_header: break

            header = Header(serialialized_header)
            if header.protocol == 1:




            if data == "TESTE":
                '''
                import subprocess
                p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
                (output, err) = p.communicate()
                print "Today is", output

                ou

                out = check_output(["ntpq", "-p"])
                '''

                out = subprocess.check_output('ps')

                print 'Received data: ', data
                print 'Command ps executed: ', out


        conn.close()
        break