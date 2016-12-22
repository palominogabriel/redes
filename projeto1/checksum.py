def checksum(ck_header):

    size = len(ck_header)
    cksum = 0
    pointer = 0

    #O loop principal adiciona os conjunto de 2 bytes.Eles são primeiro convertidos em strings e
    #depois concatenados juntos, convertidos em inteiros e, em seguida, adicionados à soma.
    while size > 1:
        cksum += int((str("%02x" % (ck_header[pointer],)) +
                      str("%02x" % (ck_header[pointer + 1],))), 16)
        size -= 2
        pointer += 2
    if size: #Possibilidade do tamanho do header ser impar
        cksum += ck_header[pointer]

    cksum = (cksum >> 16) + (cksum & 0xffff)
    cksum += (cksum >>16)

    return (~cksum) & 0xFFFF

#converte um cabeçalho serializado em uma lista de words de 16 bits
def serialToList(serialized):
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

#print("Checksum : %x" % (checksum(serialToList(serialized)),))