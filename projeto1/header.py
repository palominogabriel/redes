#!/usr/bin/env python
# coding=utf-8
import binascii

class Header():
    def __init__(self, header=None):
        self.__version_len = 4  # bits
        self.__IHL_len = 4  # bits
        self.__type_service_len = 8  # bits
        self.__total_length_len = 16  # bits
        self.__identification_len = 16  # bits
        self.__flags_len = 3  # bits
        self.__fragment_offset_len = 13  # bits
        self.__time_live_len = 8  # bits
        self.__protocol_len = 8  # bits
        self.__checksum_len = 16  # bits
        self.__source_addr_len = 32  # bits
        self.__destination_addr_len = 32  # bits
        self.__options_len = 0  # bits

        if header == None:
            self.__version = 2
            self.__IHL = 5
            self.__type_service = 0
            self.__total_length = 160 # Options vazio
            self.__identification = 10 # Numero de sequencia escolhido 1010b
            self.__flags = 0 # Requisição
            self.__fragment_offset = 0
            self.__time_live = 10
            self.__protocol = 1 # ps
            self.__checksum = 0 # Precisa Calcular
            self.__source_addr = '127.0.0.1'
            self.__destination_addr = '127.0.0.1'
            self.__options = ''
        else:
            self.break_header(header)

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, value):
        self.__version = value

    @property
    def IHL(self):
        return self.__IHL

    @IHL.setter
    def IHL(self, value):
        self.__IHL = value

    @property
    def type_service(self):
        return self.__type_service

    @type_service.setter
    def type_service(self, value):
        self.__type_service = value

    @property
    def total_length(self):
        return self.__total_length

    @total_length.setter
    def total_length(self, value):
        self.__total_length = value

    @property
    def identification(self):
        return self.__identification

    @identification.setter
    def identification(self, value):
        self.__identification = value

    @property
    def flags(self):
        return self.__flags

    @flags.setter
    def flags(self, value):
        self.__flags = value

    @property
    def fragment_offset(self):
        return self.__fragment_offset

    @fragment_offset.setter
    def fragment_offset(self, value):
        self.__fragment_offset = value

    @property
    def time_live(self):
        return self.__time_live

    @time_live.setter
    def time_live(self, value):
        self.__time_live = value

    @property
    def protocol(self):
        return self.__protocol

    @protocol.setter
    def protocol(self, value):
        self.__protocol = value

    @property
    def checksum(self):
        return self.__checksum

    @checksum.setter
    def checksum(self, value):
        self.__checksum = value

    @property
    def source_addr(self):
        return self.__source_addr

    @source_addr.setter
    def source_addr(self, value):
        self.__source_addr = value

    @property
    def destination_addr(self):
        return self.__destination_addr

    @destination_addr.setter
    def destination_addr(self, value):
        self.__destination_addr = value

    @property
    def options(self):
        return self.__options

    @options.setter
    def options(self, value):
        self.__options = value
        if value != '':
            self.options_len = len(value) * 8
        else:
            self.options_len = 0


    #Fields Length

    @property
    def version_len(self):
        return self.__version_len

    @property
    def IHL_len(self):
        return self.__IHL_len

    @property
    def type_service_len(self):
        return self.__type_service_len

    @property
    def total_length_len(self):
        return self.__total_length_len

    @property
    def identification_len(self):
        return self.__identification_len

    @property
    def flags_len(self):
        return self.__flags_len

    @property
    def fragment_offset_len(self):
        return self.__fragment_offset_len

    @property
    def time_live_len(self):
        return self.__time_live_len

    @property
    def protocol_len(self):
        return self.__protocol_len

    @property
    def checksum_len(self):
        return self.__checksum_len

    @property
    def source_addr_len(self):
        return self.__source_addr_len

    @property
    def destination_addr_len(self):
        return self.__destination_addr_len

    @property
    def options_len(self):
        return self.__options_len

    @options_len.setter
    def options_len(self,value):
        self.__options_len = value

    def addr_to_bin(self, addr=''):
        if addr != '':
            splited_addr = addr.split('.')
            binary = ''
            for spt in splited_addr:
                binary += str(format(int(spt), '#010b').replace('0b',''))
            return binary
        else:
            return addr

    def bin_to_addr(self,addr=''):
        if addr != '':
            n1 = int(addr[:8],2)
            n2 = int(addr[8:16],2)
            n3 = int(addr[16:24],2)
            n4 = int(addr[24:32],2)
            return str(n1) + '.' + str(n2) + '.' + str(n3) + '.' + str(n4)
        else:
            return addr

    def cksum(self, ck_header):

        size = len(ck_header)
        cksum = 0
        pointer = 0

        # O loop principal adiciona os conjunto de 2 bytes.Eles são primeiro convertidos em strings e
        # depois concatenados juntos, convertidos em inteiros e, em seguida, adicionados à soma.
        while size > 1:
            cksum += int((str("%02x" % (ck_header[pointer],)) +
                          str("%02x" % (ck_header[pointer + 1],))), 16)
            size -= 2
            pointer += 2
        if size:  # Possibilidade do tamanho do header ser impar
            cksum += ck_header[pointer]

        cksum = (cksum >> 16) + (cksum & 0xffff)
        cksum += (cksum >> 16)

        return (~cksum) & 0xFFFF

    # converte um cabeçalho serializado em uma lista de words de 16 bits
    def serialToList(self, serialized):
        palavra = []
        hexas = {}
        j = 0
        for i in serialized:
            palavra.append(i)
            if (len(palavra) == 16):
                palavra = "".join(palavra)
                hexas[j] = int(palavra, 2)
                palavra = []
                j += 1
        return hexas

    def make_header(self):
        # Falta calcular checksum antes de criar o pacote
        if self.options != '':
            self.options_len = len(self.options) * 8
            self.total_length = 160 + self.options_len

        header = ''
        header += str(format(self.version,'#0' + str(self.version_len + 2) + 'b').replace('0b',''))
        header += str(format(self.IHL,'#0' + str(self.IHL_len + 2) + 'b').replace('0b',''))
        header += str(format(self.type_service, '#0' + str(self.type_service_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.total_length, '#0' + str(self.total_length_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.identification, '#0' + str(self.identification_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.flags, '#0' + str(self.flags_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.fragment_offset, '#0' + str(self.fragment_offset_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.time_live, '#0' + str(self.time_live_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.protocol, '#0' + str(self.protocol_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.checksum, '#0' + str(self.checksum_len + 2) + 'b').replace('0b', ''))
        header += self.addr_to_bin(self.source_addr)
        header += self.addr_to_bin(self.destination_addr)
        if self.options != '':
            header += str(format(int(binascii.hexlify(self.options), 16), '#0' + str(self.options_len + 2) + 'b').replace('0b', ''))
        return header

    def make_header_cs(self):
        serial = self.make_header()
        list16 = self.serialToList(serial)
        self.checksum = self.cksum(list16)

        if self.options != '':
            self.options_len = len(self.options) * 8
            self.total_length = 160 + self.options_len

        header = ''
        header += str(format(self.version, '#0' + str(self.version_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.IHL, '#0' + str(self.IHL_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.type_service, '#0' + str(self.type_service_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.total_length, '#0' + str(self.total_length_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.identification, '#0' + str(self.identification_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.flags, '#0' + str(self.flags_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.fragment_offset, '#0' + str(self.fragment_offset_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.time_live, '#0' + str(self.time_live_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.protocol, '#0' + str(self.protocol_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.checksum, '#0' + str(self.checksum_len + 2) + 'b').replace('0b', ''))
        header += self.addr_to_bin(self.source_addr)
        header += self.addr_to_bin(self.destination_addr)
        if self.options != '':
            header += str(
                format(int(binascii.hexlify(self.options), 16), '#0' + str(self.options_len + 2) + 'b').replace('0b',
                                                                                                                ''))
        return header


    def break_header(self,header):
        self.version = int(header[:4],2)
        self.IHL = int(header[4:8],2)
        self.type_service = int(header[8:16],2)
        self.total_length = int(header[16:32],2)
        self.identification = int(header[32:48],2)
        self.flags = int(header[48:51],2)
        self.fragment_offset = int(header[51:64],2)
        self.time_live = int(header[64:72],2)
        self.protocol = int(header[72:80],2)
        self.checksum = int(header[80:96],2)
        self.source_addr = self.bin_to_addr(header[96:128])
        self.destination_addr = self.bin_to_addr(header[128:160])
        if len(header) > 160:
            self.options = binascii.unhexlify('%x' % int(header[160:],2))
        else:
            self.options = ''

'''#teste checksum
head = Header()
head.flags = 1
headS = head.make_header_cs()
headB = Header()
headB.break_header(headS)
headB.checksum = 0
#headB.flags = 0
print("Checksum de Head: ", head.checksum, "Flags: ", head.flags)
print("Checksum de HeadB: ", headB.cksum(headB.serialToList(headB.make_header())), "Flags: ", headB.flags)'''



