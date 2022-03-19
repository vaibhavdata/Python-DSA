def min(arr):
    if len(arr)==0:
        minEle = -1
    else:
        arr.sort()
        minEle =arr[0]
    return minEle
def max(arr):
    if len(arr)==0:
        maxEle = -1
    else:
        arr.sort()
        maxEle = arr[-1]
    return maxEle
arr = [1,2,4,5,6,7,8,19,-10]
min = min(arr)
print(min)
print()
max = max(arr)
print(max)

print("second method for find max and min in ele")
import sys
def min(arr):
    if len(arr)==0:
        minEle = -1
    else:
        minEle =sys.maxsize
        for i in arr:
            if i<minEle:
                minEle =i
    return minEle
def max(arr):
    if len(arr)==0:
        maxEle = -1
    else:
        maxEle = -sys.maxsize
        for i in arr:
            if i>maxEle:
                maxEle =i
    return maxEle

arr = [1,2,4,5,6,7,8,19,-10,20]
min = min(arr)
print(min)
print()
max = max(arr)
print(max)
