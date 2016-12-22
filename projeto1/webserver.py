#!/usr/bin/env python
import cgi
import cgitb
import socket
from maquina import Maquina
from header import Header
import binascii

cgitb.enable()

form = cgi.FieldStorage()

maq1 = Maquina(1)

maq1.ps = form.getvalue('maq1_ps')
maq1.ps_args = form.getvalue('maq1-ps') if form.getvalue('maq1-ps') else ''
maq1.df = form.getvalue('maq1_df')
maq1.df_args = form.getvalue('maq1-df') if form.getvalue('maq1-ds') else ''
maq1.finger = form.getvalue('maq1_finger')
maq1.finger_args = form.getvalue('maq1-finger') if form.getvalue('maq1-finger') else ''
maq1.uptime = form.getvalue('maq1_uptime')
maq1.uptime_args = form.getvalue('maq1-uptime') if form.getvalue('maq1-uptime') else ''

maq2 = Maquina(2)

maq2.ps = form.getvalue('maq2_ps')
maq2.ps_args = form.getvalue('maq2-ps') if form.getvalue('maq2-ps') else ''
maq2.df = form.getvalue('maq2_df')
maq2.df_args = form.getvalue('maq2-df') if form.getvalue('maq2-df') else ''
maq2.finger = form.getvalue('maq2_finger')
maq2.finger_args = form.getvalue('maq2-finger') if form.getvalue('maq2-finger') else ''
maq2.uptime = form.getvalue('maq2_uptime')
maq2.uptime_args = form.getvalue('maq2-uptime') if form.getvalue('maq2-uptime') else ''

maq3 = Maquina(3)

maq3.ps = form.getvalue('maq3_ps')
maq3.ps_args = form.getvalue('maq3-ps') if form.getvalue('maq3-ps') else ''
maq3.df = form.getvalue('maq3_df')
maq3.df_args = form.getvalue('maq3-df') if form.getvalue('maq3-df') else ''
maq3.finger = form.getvalue('maq3_finger')
maq3.finger_args = form.getvalue('maq3-finger') if form.getvalue('maq3-finger') else ''
maq3.uptime = form.getvalue('maq3_uptime')
maq3.uptime_args = form.getvalue('maq3-uptime') if form.getvalue('maq3-uptime') else ''

print 'Content-Type: text/html;charset=utf-8\r\n\r\n'
print '<html>'
print '<head>'
print '<title>Redes - Projeto 1</title>'
print '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/css/bootstrap.min.css" integrity="sha384-AysaV+vQoT3kOAXZkl02PThvDr8HYKPZhNT5h/CXfBThSRXQ6jW5DO2ekP5ViFdi" crossorigin="anonymous">'
print '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/js/bootstrap.min.js" integrity="sha384-BLiI7JTZm+JWlgKa0M0kGRpJbF2J8q+qreVrKBC47e3K6BW78kGLrCkeRX6I9RoK" crossorigin="anonymous"></script>'
print '</head>'
print '<body style="background-image:url(http://www.evohosting.co.uk/wp-content/uploads/2014/12/Pattern-christmas-elements-seamless-vector-011-e1418392819694.jpg); background-repeat: repeat;">'
print '<div style="background-color: #ffffff; height:100%; width:100%; opacity: 0.9; z-index:-1; position: fixed;"> </div>'

#MAQUINA 1
header_maq1_ps = Header()
header_maq1_df = Header()
header_maq1_finger = Header()
header_maq1_uptime = Header()

header_maq1_ps.protocol = 1
header_maq1_ps.options = maq1.ps_args
header_maq1_df.protocol = 2
header_maq1_df.options = maq1.df_args
header_maq1_finger.protocol = 3
header_maq1_finger.options = maq1.finger_args
header_maq1_uptime.protocol = 4
header_maq1_uptime.options = maq1.uptime_args

#MAQUINA 2
header_maq2_ps = Header()
header_maq2_df = Header()
header_maq2_finger = Header()
header_maq2_uptime = Header()

header_maq2_ps.protocol = 1
header_maq2_ps.options = maq2.ps_args
header_maq2_df.protocol = 2
header_maq2_df.options = maq2.df_args
header_maq2_finger.protocol = 3
header_maq2_finger.options = maq2.finger_args
header_maq2_uptime.protocol = 4
header_maq2_uptime.options = maq2.uptime_args


#MAQUINA 3
header_maq3_ps = Header()
header_maq3_df = Header()
header_maq3_finger = Header()
header_maq3_uptime = Header()

header_maq3_ps.protocol = 1
header_maq3_ps.options = maq3.ps_args
header_maq3_df.protocol = 2
header_maq3_df.options = maq3.df_args
header_maq3_finger.protocol = 3
header_maq3_finger.options = maq3.finger_args
header_maq3_uptime.protocol = 4
header_maq3_uptime.options = maq3.uptime_args


ip = '127.0.0.1'
pm1 = 9001
pm2 = 9002
pm3 = 9003
buff_size = 10024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((ip,pm1))
except socket.error:
    print('connection error')

if maq1.ps != '':
    s.send(header_maq1_ps.make_header())
    maq1.ps_result = s.recv(1024)
if maq1.df != '':
    s.send(header_maq1_df.make_header())
    maq1.df_result = s.recv(buff_size)
if maq1.finger != '':
    s.send(header_maq1_finger.make_header())
    maq1.finger_result = s.recv(buff_size)
if maq1.uptime != '':
    s.send(header_maq1_uptime.make_header())
    maq1.uptime_result = s.recv(buff_size)


#Maquina2
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((ip, pm2))
except socket.error:
    print('connection error')

if maq2.ps != '':
    s.send(header_maq2_ps.make_header())
    maq2.ps_result = s.recv(buff_size)
if maq2.df != '':
    s.send(header_maq2_df.make_header())
    maq2.df_result = s.recv(buff_size)
if maq2.finger != '':
    s.send(header_maq2_finger.make_header())
    maq2.finger_result = s.recv(buff_size)
if maq2.uptime != '':
    s.send(header_maq2_uptime.make_header())
    maq2.uptime_result = s.recv(buff_size)


#Maquina3
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((ip, pm3))
except socket.error:
    print('connection error')

if maq3.ps != '':
    s.send(header_maq3_ps.make_header())
    maq3.ps_result = s.recv(buff_size)
if maq3.df != '':
    s.send(header_maq3_df.make_header())
    maq3.df_result = s.recv(buff_size)
if maq3.finger != '':
    s.send(header_maq3_finger.make_header())
    maq3.finger_result = s.recv(buff_size)
if maq3.uptime != '':
    s.send(header_maq3_uptime.make_header())
    maq3.uptime_result = s.recv(buff_size)


'''
try:

    # Send data
    s.sendall(header_maq1_ps.make_header())

    # Look for the response
    amount_received = 0
    amount_expected = len(header_maq1_ps.make_header())

    while amount_received < amount_expected:
        data = s.recv(buff_size)
        amount_received += len(data)

    maq1.ps_result = s.recv(buff_size)

finally:
    print >> sys.stderr, 'closing socket'
    sock.close()

'''

s.close()

print maq1
print maq2
print maq3

print '</body>'
print '</html>'
