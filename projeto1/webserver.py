#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()

class Maquina():
    def __init__(self, id=None, ps=None, ps_args=None, df=None, df_args=None, finger=None, finger_args=None, uptime=None, uptime_args=None):
        self.__id = id
        self.__ps = ps
        self.__ps_args = ps_args
        self.__df = df
        self.__df_args = df_args
        self.__finger = finger
        self.__finger_args = finger_args
        self.__uptime = uptime
        self.__uptime_args = uptime_args

    @property
    def id(self):
        return str(self.__id)

    @id.setter
    def id(self,value):
        self.__id = value

    @property
    def ps(self):
        if self.__ps == 'None':
            return ''
        else:
            return str(self.__ps)

    @ps.setter
    def ps(self,value):
        self.__ps = value

    @property
    def ps_args(self):
        return self.__ps_args

    @ps_args.setter
    def ps_args(self, value):
        self.__ps_args = value

    def __str__(self):
        return 'Maquina' + self.id + 'ps=' + self.ps


mq1 = Maquina(1)


print("Content-Type: text/html;charset=utf-8\r\n\r\n")
print("<html>")
print("<title>TESTE</title>")

mq1.id = 3
print(mq1.id + 'ps=' + mq1.ps)

form = cgi.FieldStorage()


print ("<br><br>" + str(form.getvalue("maq1_ps")))
print ("<br>" + str(form.getvalue("maq1-ps")))

print("</html>")
