def insert(arr,alpha):
    if len(arr)==0 or arr[-1]<alpha:
        arr.append(alpha)
        return 
    op = arr.pop(-1)
    insert(arr,alpha)
    arr.append(op)
def sort(arr):
    if len(arr)==1:
        return 
    alpha = arr.pop(0)
    sort(arr)
    insert(arr,alpha)
arr = [1,2,4,5,6,3,0,8,2,4,6]
sort(arr)
print(arr)



