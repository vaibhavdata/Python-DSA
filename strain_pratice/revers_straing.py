def reverseStrain(ip_str):
    return ip_str[::-1]
ip_str = "geeks for"
flag = reverseStrain(ip_str)
print(flag)
print()


# second method
def reverseStraing2(ip_str):
    ip_str = list(ip_str)
    i=0
    j = len(ip_str) -1
    while i<j:
        ip_str[i],ip_str[j]=ip_str[j],ip_str[i]
        i +=1
        j -=1
    ip_str = "".join(ip_str)
    return ip_str
ip_str = "geeks for"
flag = reverseStraing2(ip_str)
print(flag)
