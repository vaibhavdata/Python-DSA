def binaryserachdescing(arr,ele,start,end):
    ind = -1
    while start <=end:
        mid = start+ (end-start)//2
        if arr[mid]==ele:
            ind = mid
            break
        elif ele>arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return ind

arr = [6,5,4,3,7,0]
ele =7
start =0 
end = len(arr) -1
index = binaryserachdescing(arr,ele,start,end)
print(index)