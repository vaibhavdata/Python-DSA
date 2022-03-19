from itertools import count


def removegivenchar(ip_str,ele):
    ip_str = list(ip_str)
    i =0
    while i<len(ip_str):
        if ip_str[i]==ele:
            ip_str.pop(i)
        else:
            i +=1
    ip_str =''.join(ip_str)
    return ip_str
    
ip_str = "abcdfgr"
ele = 'r'
flag = removegivenchar(ip_str,ele)
print(flag)