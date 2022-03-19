def getelementbyindex(arr,idx):
    if idx >len(arr):
        return -1
    else:
        return arr[idx]

arr = [2,3,4,56]
idx = 2
flag = getelementbyindex(arr,idx)
print(flag)
