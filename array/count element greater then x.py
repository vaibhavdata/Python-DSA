def countgreterthenX(arr,n,x):
    count =0
    for i in range(n):
        if arr[i] >x:
            count +=1
    return count
arr =[2,3,4,5,6,7,8]
n= len(arr)-1
x= 4
flag = countgreterthenX(arr,n,x)
print(flag)