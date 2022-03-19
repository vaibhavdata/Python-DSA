def rotateArray(arr,n):
    arr[:]=arr[n:]+arr[:n]
    return arr
arr = [2,3,4,1,0]
n= 1
rotateArray(arr,n)
print(arr)