def remove_agivenChar(ip_str,chr):
    ip_str = list(ip_str)
    i = 0
    while i< len(ip_str):
        if ip_str[i] ==chr:
            ip_str.pop(i)
        else:
            i +=1
    ip_str = "".join(ip_str)
    return ip_str
ip_str = "abcdefgghi"
chr = 'g'
op_str = remove_agivenChar(ip_str,chr)
print(op_str)
