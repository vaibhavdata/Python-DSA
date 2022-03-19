import sys
def mostElement(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i]=count[i]+1
        else:
            count[i]=1
    ans =-1
    max = -sys.maxsize
    for char,coun in count.items():
        if coun > max:
            max= coun
            ans = char
    return ans
arr= [3,4,5,5,5,2,2,2,2,7,7,7,78,8,8,9,9]
flag = mostElement(arr)
print(flag)