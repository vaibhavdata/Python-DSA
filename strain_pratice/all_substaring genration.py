from ipaddress import ip_address


def allSubstraing(ip_str):
    #ip_str = list(ip_str)
    n = len(ip_str)
    sublist =[]
    for i in range(n):
        for j in range(i+1,n+1):
            sublist.append(ip_str[i:j])
    return sublist
ip_str = 'abc'
flag = allSubstraing(ip_str)
print(flag)

print("second method substraing generation")
def allSubStraing2(ip_str):
    #ip_str = list(ip_str)
    n= len(ip_str)
    sublist = []
    for i in range(n):
        temp =[]
        for j in range(i,n):
            temp.append(ip_str[j])
            alpha = ''.join(temp)
            sublist.append(alpha)
    return sublist
ip_str = 'abd'
flag = allSubStraing2(ip_str)
print(flag)
    