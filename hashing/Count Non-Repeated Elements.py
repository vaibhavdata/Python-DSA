from collections import Counter
def countNonRepeElement(arr):
    cnt = Counter(arr)
    c = 0
    for fre in cnt.values():
        if fre ==1:
            c +=1
    return c
arr = [2,3,4,4,5,6,6,7,8,9,10,10,11]

index =countNonRepeElement(arr)
print(index)

    