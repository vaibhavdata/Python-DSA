from collections import Counter

def printNonRepeated_elements(arr):
    count = Counter(arr)
    lst =[str(x) for x in arr if count[x]==1]
    return lst
arr = [2,3,4,4,3,5,6,7,8,8,10,12,1,10,12,7,15]
index = printNonRepeated_elements(arr)
print(index)
