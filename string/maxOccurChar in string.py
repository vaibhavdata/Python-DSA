import sys
def maxOccurChar(ip_str):
    count = {}
    for i in ip_str:
        if i in count:
            count[i] = count[i]+1
        else:
            count[i] =1
    max= -sys.maxsize
    ans = ""
    for char,cou in count.items():
        if cou >max:
            max= cou
            ans = char
    return ans
ip_str = "abbcccddddeeffffffgggggggg"
print(maxOccurChar(ip_str))

print("second method")
# second method of maxx occurah
def maxOccurChar2(ip_str):
    count = []
    for  i in list(set(ip_str)):
        c =0
        for j in ip_str:
            if i==j:
                c =c+1
        count.append([i,c])
    max= -sys.maxsize
    ans = ""
    for char,cou in count:
        if cou >max:
            max= cou
            ans = char
    return ans
    
ip_str = "abbcccddddeeffffffgggggggg"
op_str =maxOccurChar2(ip_str)
print(op_str)