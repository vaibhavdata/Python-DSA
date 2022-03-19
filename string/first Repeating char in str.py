def  firstRepeating(ip_str):
    count ={}
    for i in ip_str:
        if i in count:
            count[i]=count[i]+1
        else:
            count[i] =1
    ans =""
    for char,coun in count.items():
        if coun >1:
            ans = char
            break
    return ans
ip_str = "abbbccddde"
op = firstRepeating(ip_str)
print(op)

print("second method in repiting char")
def firstRepeating2(ip_str):
    count = []
    for i in list(set(ip_str)):
        c = 0
        for j in ip_str:
            if i==j:
                c +=1
        count.append([i,c])
    ans =''
    for char,coun in count:
        if coun >1:
            ans= char
            break
    return ans
ip_str = "abbbccddde"
op = firstRepeating2(ip_str)
print(op)