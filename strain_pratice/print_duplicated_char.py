def printDuplicated(ip_str):
    count ={}
    for i in ip_str:
        if i in count:
            count[i]=count[i]+1
        else:
            count[i]=1
    ans =[]
    for char,coun in count.items():
        if coun >1:
            ans.append(char)
    return ans
ip_str ="abcddeeffgg"
flag = printDuplicated(ip_str)
print(flag)