class Header():
    def __init__(self):
        self.__h_version = 2
        self.__h_IHL = 0
        self.__h_type_service = 0
        self.__h_total_length = 0
        self.__h_identification = 0
        self.__h_flags = 0
        self.__h_fragment_offset = 0
        self.__h_time_live = 1
        self.__h_protocol = 0
        self.__h_checksum = 0
        self.__h_source_addr = ''
        self.__h_destination_addr = ''
        self.__h_options = ''
        self.__h_paddin = 0
        self.__h_version_len = 4  # bits
        self.__h_IHL_len = 4  # bits
        self.__h_type_service_len = 8  # bits
        self.__h_total_length_len = 16  # bits
        self.__h_identification_len = 16  # bits
        self.__h_flags_len = 3  # bits
        self.__h_fragment_offset_len = 13  # bits
        self.__h_time_live_len = 8  # bits
        self.__h_protocol_len = 8  # bits
        self.__h_checksum_len = 16  # bits
        self.__h_source_addr_len = 32  # bits
        self.__h_destination_addr_len = 32  # bits
        self.__h_options_len = 24  # bits
        self.__h_paddin_len = 8  # bits
        self.__header = list()

    @property
    def h_version(self):
        return self.__h_version

    @h_version.setter
    def h_version(self, value):
        self.__h_version = value

    @property
    def h_IHL(self):
        return self.__h_IHL

    @h_IHL.setter
    def h_IHL(self, value):
        self.__h_IHL = value

    @property
    def h_type_service(self):
        return self.__h_type_service

    @h_type_service.setter
    def h_type_service(self, value):
        self.__h_type_service = value

    @property
    def h_total_length(self):
        return self.__h_total_length

    @h_total_length.setter
    def h_total_length(self, value):
        self.__h_total_length = value

    @property
    def h_identification(self):
        return self.__h_identification

    @h_identification.setter
    def h_identification(self, value):
        self.__h_identification = value

    @property
    def h_flags(self):
        return self.__h_flags

    @h_flags.setter
    def h_flags(self, value):
        self.__h_flags = value

    @property
    def h_fragment_offset(self):
        return self.__h_fragment_offset

    @h_fragment_offset.setter
    def h_fragment_offset(self, value):
        self.__h_fragment_offset = value

    @property
    def h_time_live(self):
        return self.__h_time_live

    @h_time_live.setter
    def h_time_live(self, value):
        self.__h_time_live = value

    @property
    def h_protocol(self):
        return self.__h_protocol

    @h_protocol.setter
    def h_protocol(self, value):
        self.__h_protocol = value

    @property
    def h_checksum(self):
        return self.__h_checksum

    @h_checksum.setter
    def h_checksum(self, value):
        self.__h_checksum = value

    @property
    def h_source_addr(self):
        return self.__h_source_addr

    @h_source_addr.setter
    def h_source_addr(self, value):
        self.__h_source_addr = value

    @property
    def h_destination_addr(self):
        return self.__h_destination_addr

    @h_destination_addr.setter
    def h_destination_addr(self, value):
        self.__h_destination_addr = value

    @property
    def h_options(self):
        return self.__h_options

    @h_options.setter
    def h_options(self, value):
        self.__h_options = value

    @property
    def h_padding(self):
        return self.__h_padding

    @h_padding.setter
    def h_padding(self, value):
        self.__h_padding = value

    @property
    def h_version_len(self):
        return self.__h_version_len

    @property
    def h_IHL_len(self):
        return self.__h_IHL_len

    @property
    def h_type_service_len(self):
        return self.__h_type_service_len

    @property
    def h_total_length_len(self):
        return self.__h_total_length_len

    @property
    def h_identification_len(self):
        return self.__h_identification_len

    @property
    def h_flags_len(self):
        return self.__h_flags_len

    @property
    def h_fragment_offset_len(self):
        return self.__h_fragment_offset_len

    @property
    def h_time_live_len(self):
        return self.__h_time_live_len

    @property
    def h_protocol_len(self):
        return self.__h_protocol_len

    @property
    def h_checksum_len(self):
        return self.__h_checksum_len

    @property
    def h_source_addr_len(self):
        return self.__h_source_addr_len

    @property
    def h_destination_addr_len(self):
        return self.__h_destination_addr_len

    @property
    def h_options_len(self):
        return self.__h_options_len

    def make_header(self):
        self.__header.append(str(format(self.__h_version,'#0' + str(self.__h_version_len + 2) + 'b').replace('0b','')))
        self.__header[0] += str(format(self.__h_IHL,'#0' + str(self.__h_IHL_len + 2) + 'b').replace('0b',''))
        self.__header[0] += str(format(self.__h_type_service, '#0' + str(self.__h_type_service_len + 2) + 'b').replace('0b', ''))
        self.__header[0] += str(format(self.__h_total_length, '#0' + str(self.__h_total_length_len + 2) + 'b').replace('0b', ''))
        self.__header.append(str(format(self.__h_identification, '#0' + str(self.__h_identification_len + 2) + 'b').replace('0b', '')))
        self.__header[1] += str(format(self.__h_flags, '#0' + str(self.__h_flags_len + 2) + 'b').replace('0b', ''))
        self.__header[1] += str(format(self.__h_fragment_offset, '#0' + str(self.__h_fragment_offset_len + 2) + 'b').replace('0b', ''))
        self.__header.append(str(format(self.__h_time_live, '#0' + str(self.__h_time_live_len + 2) + 'b').replace('0b', '')))
        self.__header[2] += str(format(self.__h_protocol, '#0' + str(self.__h_protocol_len + 2) + 'b').replace('0b', ''))
        self.__header[2] += str(format(self.__h_checksum, '#0' + str(self.__h_checksum_len + 2) + 'b').replace('0b', ''))
        self.__header.append(str(format(self.__h_source_addr, '#0' + str(self.__h_source_addr_len + 2) + 'b').replace('0b', '')))
        self.__header.append(str(format(self.__h_destination_addr, '#0' + str(self.__h_destination_addr_len + 2) + 'b').replace('0b', '')))
        self.__header.append(str(format(self.__h_options, '#0' + str(self.__h_options_len + 2) + 'b').replace('0b', '')))
        self.__header[5] += str(format(self.__h_paddin, '#0' + str(self.__h_paddin_len + 2) + 'b').replace('0b', ''))

        header_serialized = ''
        for head in self.__header:
            header_serialized += str(head)

        return header_serialized