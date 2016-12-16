#!/usr/bin/env python
import cgi
import cgitb
from maquina import Maquina
cgitb.enable()

form = cgi.FieldStorage()

maq1 = Maquina(1)

maq1.ps = form.getvalue('maq1_ps')
maq1.ps_args = form.getvalue('maq1-ps')
maq1.df = form.getvalue('maq1_df')
maq1.df_args = form.getvalue('maq1-df')
maq1.finger = form.getvalue('maq1_finger')
maq1.finger_args = form.getvalue('maq1-finger')
maq1.uptime = form.getvalue('maq1_uptime')
maq1.uptime_args = form.getvalue('maq1-uptime')

maq2 = Maquina(2)

maq2.ps = form.getvalue('maq2_ps')
maq2.ps_args = form.getvalue('maq2-ps')
maq2.df = form.getvalue('maq2_df')
maq2.df_args = form.getvalue('maq2-df')
maq2.finger = form.getvalue('maq2_finger')
maq2.finger_args = form.getvalue('maq2-finger')
maq2.uptime = form.getvalue('maq2_uptime')
maq2.uptime_args = form.getvalue('maq2-uptime')

maq3 = Maquina(3)

maq3.ps = form.getvalue('maq3_ps')
maq3.ps_args = form.getvalue('maq3-ps')
maq3.df = form.getvalue('maq3_df')
maq3.df_args = form.getvalue('maq3-df')
maq3.finger = form.getvalue('maq3_finger')
maq3.finger_args = form.getvalue('maq3-finger')
maq3.uptime = form.getvalue('maq3_uptime')
maq3.uptime_args = form.getvalue('maq3-uptime')

print 'Content-Type: text/html;charset=utf-8\r\n\r\n'
print '<html>'
print '<head>'
print '<title>Redes - Projeto 1</title>'
print '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/css/bootstrap.min.css" integrity="sha384-AysaV+vQoT3kOAXZkl02PThvDr8HYKPZhNT5h/CXfBThSRXQ6jW5DO2ekP5ViFdi" crossorigin="anonymous">'
print '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/js/bootstrap.min.js" integrity="sha384-BLiI7JTZm+JWlgKa0M0kGRpJbF2J8q+qreVrKBC47e3K6BW78kGLrCkeRX6I9RoK" crossorigin="anonymous"></script>'
print '</head>'
print '<body style="background-image:url(http://www.evohosting.co.uk/wp-content/uploads/2014/12/Pattern-christmas-elements-seamless-vector-011-e1418392819694.jpg); background-repeat: repeat;">'
print '<div style="background-color: #ffffff; height:100%; width:100%; opacity: 0.9; z-index:-1; position: fixed;"> </div>'

print maq1
print maq2
print maq3

print '</body>'
print '</html>'
