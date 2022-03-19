def binaryserachasc(arr,ele,start,end):
    ind= -1 
    while start <end:
        mid  = start + (end - start)//2
        if arr[mid] ==ele:
            ind = mid
            break
        elif ele < arr[mid]:
            end = mid -1
        else:
            start = mid + 1
    return ind

        

arr = [3,4,5,6,2,9,0,4]
ele = 2
start = 0
end = len(arr) -1
index =binaryserachasc(arr,ele,start,end)
print(index)