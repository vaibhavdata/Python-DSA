def countmaj(arr,n):
    count ={}
    for i in arr:
        if i in count:
            count[i]=count[i]+1
        else:
            count[i]=1
    for k,v in count.items():
        if v>n/2:
            return k
        return -1
arr = [1,2,3,4,5,5,5,5,5,5,3,2,3,6,5,4,5,4,4,4,6,6,6]
n =2
flag =countmaj(arr,n)
print(flag)