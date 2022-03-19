def sortedarray1(arr):
    if len(arr)==0 or len(arr)==1:
        return True
    return arr[0] <arr[1] and sortedarray1(arr[1:])

arr =[4,5,2,10,6,9,1]
flag = sortedarray1(arr)
print(flag)