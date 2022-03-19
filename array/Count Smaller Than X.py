
def countSmaller(arr,n,x):
    count =0
    for i in range(n):
        if arr[i] <x:
            count +=1
    return count
arr =[2,3,4,5,7,2]
n= len(arr)-1
x =4
flag = countSmaller(arr,n,x)
print(flag)
