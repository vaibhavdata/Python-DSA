from itertools import count


def isallUnique(ip_str):
    unique_all = set(ip_str)
    if len(ip_str)==len(unique_all):
        return True
    else:
        return False
ip_str = "abccddvv"
flag = isallUnique(ip_str)
print(flag)

print("second method")
def isallunique2(ip_str):
    count ={}
    for i in ip_str:
        if i in count:
            count[i]=count[i]+1
        else:
            count[i]=1
    for char,coun in count.items():
        if coun !=1:
            return False
        return True
ip_str="abcdefghk"
flag = isallunique2(ip_str)
print(flag)