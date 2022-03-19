def firstOffurance(arr,ele,start,end):
    ind = -1
    while start<end:
        mid = (start+end)//2
        if ele==arr[mid]:
            ind =mid
            end = mid-1
        elif ele <arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return ind
def lastOffurance(arr,ele,start,end):
    ind =-1
    while start<end:
        mid = (start+end)//2
        if ele==arr[mid]:
            ind =mid
            start = mid+1
        elif ele<arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return ind
arr = [0,1,1,1,2,2,2,2,3,3,3,4,4]
ele = 2
start = 0
end = len(arr)-1
first= firstOffurance(arr,ele,start,end)
last = lastOffurance(arr,ele,start,end)
count = last - first+1
print(count)