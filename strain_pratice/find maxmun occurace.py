import sys
def findMaxOccurce(ip_str):
    count = {}
    for i in ip_str:
        if i in count:
            count[i] = count[i]+1
        else:
            count[i]=1
    max = -sys.maxsize
    ans =""
    for char,coun in count.items():
        if coun >max:
            max= coun
            ans = char
    return ans
ip_str ="abcddeeeffffffggg"
flag = findMaxOccurce(ip_str)
print(flag)
print("second method max occurace charcter ")

def findMaxOccurce2(ip_str):
    count = []
    for i in list(str(ip_str)):
        c = 0
        for j in ip_str:
            if i ==j:
                c +=1
        count.append([i,c])
    max = -sys.maxsize
    ans =""
    for char,coun in count:
        if coun >max:
            max =coun
            ans = char
    return ans


ip_str ="abcddeeefgg"
flag = findMaxOccurce2(ip_str)
print(flag)
