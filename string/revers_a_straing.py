def reverseStraing(ip_str):
    ip_str = list(ip_str)
    i=0
    j = len(ip_str)-1
    while i<j:
        ip_str[i],ip_str[j]=ip_str[j],ip_str[i]
        i +=1
        j -=1
    ip_str = "".join(ip_str)
    return ip_str
ip_str = "geeks for this"
print(reverseStraing(ip_str))
print("second method")

# second method of revers straing
def reverstring(ip_str):
    return ip_str[::-1]
ip_str = "geeks for its"
print(reverstring(ip_str))