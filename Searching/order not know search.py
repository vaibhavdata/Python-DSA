# two type array sorted or not sorted

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
def binaryserach(arr,ele,start,end):
    if len(arr)==1:
        if ele==arr[0]:
            return 0
        return -1
    elif arr[0]<arr[-1]:
        return binaryserachasc(arr,ele,start,end)
    elif arr[0]>arr[-1]:
        return binaryserachdescing(arr,ele,start,end)
arr = [2,3,4,5,7,1,10,14,12]
ele = 1
start = 0
end = len(arr)-1
index =binaryserach(arr,ele,start,end)
print(index)

