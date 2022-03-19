def firstOccurence(arr,ele,start,end):
    ind =-1
    while start < end:
        mid = (start+end)//2
        if arr[mid]==ele:
            ind = mid
            end = mid -1
            print("end element",end)
        elif ele <arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return ind
arr = [0,1,1,1,2,2,2,3,3,4,4,5,5,6,6]
ele = 2
start = 0
end = len(arr) -1
index = firstOccurence(arr,ele,start,end)
print(index)
        
