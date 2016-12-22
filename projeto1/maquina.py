#!/usr/bin/env python
#teste
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
        self.__ps_result = ''
        self.__df_result = ''
        self.__finger_result = ''
        self.__uptime_result = ''

    @property
    def id(self):
        return str(self.__id)

    @id.setter
    def id(self,value):
        self.__id = value

    @property
    def ps(self):
        if self.__ps == None:
            return ''
        else:
            return str(self.__ps)

    @ps.setter
    def ps(self,value):
        self.__ps = value

    @property
    def ps_args(self):
        if self.__ps_args == None:
            return ''
        else:
            return str(self.__ps_args)

    @ps_args.setter
    def ps_args(self, value):
        self.__ps_args = value

    @property
    def df(self):
        if self.__df == None:
            return ''
        else:
            return str(self.__df)

    @df.setter
    def df(self, value):
        self.__df = value

    @property
    def df_args(self):
        if self.__df_args == None:
            return ''
        else:
            return str(self.__df_args)

    @df_args.setter
    def df_args(self, value):
        self.__df = value

    @property
    def finger(self):
        if self.__finger == None:
            return ''
        else:
            return str(self.__finger)

    @finger.setter
    def finger(self, value):
        self.__finger = value

    @property
    def finger_args(self):
        if self.__finger_args == None:
            return ''
        else:
            return str(self.__finger_args)

    @finger_args.setter
    def finger_args(self, value):
        self.__finger_args = value

    @property
    def uptime(self):
        if self.__uptime == None:
            return ''
        else:
            return str(self.__uptime)

    @uptime.setter
    def uptime(self, value):
        self.__uptime = value

    @property
    def uptime_args(self):
        if self.__uptime_args == None:
            return ''
        else:
            return str(self.uptime_args)

    @uptime_args.setter
    def uptime_args(self, value):
        self.__uptime_args = value

    @property
    def ps_result(self):
            return self.__ps_result

    @ps_result.setter
    def ps_result(self, value):
        self.__ps_result = value

    @property
    def df_result(self):
        return self.__df_result

    @df_result.setter
    def df_result(self, value):
        self.__df_result = value

    @property
    def finger_result(self):
        return self.__finger_result

    @finger_result.setter
    def finger_result(self, value):
        self.__finger_result = value

    @property
    def uptime_result(self):
        return self.__uptime_result

    @uptime_result.setter
    def uptime_result(self, value):
        self.__uptime_result = value


    def __str__(self):
        return str('<div style="width: 33%; display: inline-block; text-align: center;">'
                   + '<h2> <b> Maquina ' + str(self.id) + '</h1> </b>'
                   + '<h5> Comandos </h5>'
                   + (self.ps if self.ps else '') + (' ' + self.ps_args + '<br>' if self.ps and self.ps_args else '<br>')
                   + (self.df if self.df else '') + (' ' + self.df_args + '<br>' if self.df and self.df_args else '<br>')
                   + (self.finger if self.finger else '') + (' ' + self.finger_args + '<br>' if self.finger and self.finger_args else '<br>')
                   + (self.uptime if self.uptime else '') + (' ' + self.uptime_args + '<br> <br>' if self.uptime and self.uptime_args else '<br> <br>')
                   + '<h5> Output </h5>'
                   + self.ps_result + '<br>'
                   + self.df_result + '<br>'
                   + self.finger_result + '<br>'
                   + self.uptime_result + '<br>'
                   + '</div>'
                   )
