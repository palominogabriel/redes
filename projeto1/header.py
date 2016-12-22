#!/usr/bin/env python

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
        self.__options_len = 24  # bits
        self.__paddin_len = 8  # bits

        if header == None:
            self.__version = 2
            self.__IHL = 0
            self.__type_service = 0
            self.__total_length = 0
            self.__identification = 0
            self.__flags = 0
            self.__fragment_offset = 0
            self.__time_live = 1
            self.__protocol = 0
            self.__checksum = 0
            self.__source_addr = '127.0.0.1'
            self.__destination_addr = '127.0.0.1'
            self.__options = 0
            self.__paddin = 0
        else:
            self.break_header(header)

    @property
    def h_version(self):
        return self.__version

    @h_version.setter
    def h_version(self, value):
        self.__version = value

    @property
    def h_IHL(self):
        return self.__IHL

    @h_IHL.setter
    def h_IHL(self, value):
        self.__IHL = value

    @property
    def h_type_service(self):
        return self.__type_service

    @h_type_service.setter
    def h_type_service(self, value):
        self.__type_service = value

    @property
    def h_total_length(self):
        return self.__total_length

    @h_total_length.setter
    def h_total_length(self, value):
        self.__total_length = value

    @property
    def h_identification(self):
        return self.__identification

    @h_identification.setter
    def h_identification(self, value):
        self.__identification = value

    @property
    def h_flags(self):
        return self.__flags

    @h_flags.setter
    def h_flags(self, value):
        self.__flags = value

    @property
    def h_fragment_offset(self):
        return self.__fragment_offset

    @h_fragment_offset.setter
    def h_fragment_offset(self, value):
        self.__fragment_offset = value

    @property
    def h_time_live(self):
        return self.__time_live

    @h_time_live.setter
    def h_time_live(self, value):
        self.__time_live = value

    @property
    def h_protocol(self):
        return self.__protocol

    @h_protocol.setter
    def h_protocol(self, value):
        self.__protocol = value

    @property
    def h_checksum(self):
        return self.__checksum

    @h_checksum.setter
    def h_checksum(self, value):
        self.__checksum = value

    @property
    def h_source_addr(self):
        return self.__source_addr

    @h_source_addr.setter
    def h_source_addr(self, value):
        self.__source_addr = value

    @property
    def h_destination_addr(self):
        return self.__destination_addr

    @h_destination_addr.setter
    def h_destination_addr(self, value):
        self.__destination_addr = value

    @property
    def h_options(self):
        return self.__options

    @h_options.setter
    def h_options(self, value):
        self.__options = value

    @property
    def h_padding(self):
        return self.__padding

    @h_padding.setter
    def h_padding(self, value):
        self.__padding = value

    @property
    def h_version_len(self):
        return self.__version_len

    @property
    def h_IHL_len(self):
        return self.__IHL_len

    @property
    def h_type_service_len(self):
        return self.__type_service_len

    @property
    def h_total_length_len(self):
        return self.__total_length_len

    @property
    def h_identification_len(self):
        return self.__identification_len

    @property
    def h_flags_len(self):
        return self.__flags_len

    @property
    def h_fragment_offset_len(self):
        return self.__fragment_offset_len

    @property
    def h_time_live_len(self):
        return self.__time_live_len

    @property
    def h_protocol_len(self):
        return self.__protocol_len

    @property
    def h_checksum_len(self):
        return self.__checksum_len

    @property
    def h_source_addr_len(self):
        return self.__source_addr_len

    @property
    def h_destination_addr_len(self):
        return self.__destination_addr_len

    @property
    def h_options_len(self):
        return self.__options_len

    def addr_to_bin(self, addr=''):
        splited_addr = addr.split('.')
        binary = ''
        for spt in splited_addr:
            binary += str(format(int(spt), '#010b').replace('0b',''))
        return binary

    def make_header(self):
        header = ''
        header += str(format(self.__version,'#0' + str(self.__version_len + 2) + 'b').replace('0b',''))
        header  += str(format(self.__IHL,'#0' + str(self.__IHL_len + 2) + 'b').replace('0b',''))
        header  += str(format(self.__type_service, '#0' + str(self.__type_service_len + 2) + 'b').replace('0b', ''))
        header  += str(format(self.__total_length, '#0' + str(self.__total_length_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.__identification, '#0' + str(self.__identification_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.__flags, '#0' + str(self.__flags_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.__fragment_offset, '#0' + str(self.__fragment_offset_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.__time_live, '#0' + str(self.__time_live_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.__protocol, '#0' + str(self.__protocol_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.__checksum, '#0' + str(self.__checksum_len + 2) + 'b').replace('0b', ''))
        header += self.addr_to_bin(self.__source_addr)
        header += self.addr_to_bin(self.__destination_addr)
        header += str(format(self.__options, '#0' + str(self.__options_len + 2) + 'b').replace('0b', ''))
        header += str(format(self.__paddin, '#0' + str(self.__paddin_len + 2) + 'b').replace('0b', ''))

        return header

    def break_header(self,header):
        self.__version = header[:4]
        self.__IHL = header[4:8]
        self.__type_service = header[8:16]
        self.__total_length = header[16:32]
        self.__identification = header[32:48]
        self.__flags = header[48:52]
        self.__fragment_offset = header[52:64]
        self.__time_live = header[64:72]
        self.__protocol = header[72:80]
        self.__checksum = header[80:96]
        self.__source_addr = header[96:128]
        self.__destination_addr = header[128:160]
        self.__options = header[160:184]
        self.__paddin = header[184:192]