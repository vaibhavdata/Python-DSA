
def isAllUnique2(ip_str):
    unique_ip_str = set(ip_str)
    if len(ip_str) == len(unique_ip_str):
        return True
    return False


ip_str = 'abcd'
flag = isAllUnique2(ip_str)
print(flag)

print("second method all unique")
def isAllUnique(ip_str):
    count ={}
    for i in ip_str:
        if i in count:
            count[i]=count[i]+1
        else:
            count[i] =1
    
    for char,coun in count.items():
        if coun != 1:
            return False
    return True
ip_str ='abcdd'
flag = isAllUnique(ip_str)
print(flag)