def kthsmalles(arr,n,k,l):
    arr.sort()
    return arr[k-1]
arr = [1,2,3,4,5,6,7]
n = len(arr)-1
l =0
k = 2
flag = kthsmalles(arr,n,l,k)
print(flag)