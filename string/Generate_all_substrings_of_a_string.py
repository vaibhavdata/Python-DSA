def subStraingOfAll1(ip_str):
    sublist =[]
    n = len(ip_str)
    for i in range(n):
        for j in range(i+1,n+1):
            sublist.append(ip_str[i:j])
    return sublist

ip_str= "abc"
subList = subStraingOfAll1(ip_str)
print(subList)
print("Seconde method ")
def substring3(str):
    subList = []
    n = len(str)
    for i in range(n):
        temp = []
        for j in range(i,n):
            temp.append(str[j])
            alpha = ''.join(temp)
            subList.append(alpha)
    return subList

str= "abd"
subList = substring3(str)
print(subList)