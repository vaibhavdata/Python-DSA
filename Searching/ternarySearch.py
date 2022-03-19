def ternarySearch(arr,ele,start,end):
    ind= -1
    while start < end:
        m1 = (2*start+end)//3
        m2 = (start+end)//3
        if ele == arr[m1]:
            ind = m1
            break
        elif ele == arr[m2]:
            ind = m2
            break
        elif ele < arr[m1]:
            end = m1-1
        elif ele > arr[m2]:
            start = m2+1
        else:
            start = m1+1
            end = m2-1
    return ind



arr = [2,3,4,5,6,7,8,9,10]
ele = 7
start = 0
end = len(arr) -1
index =ternarySearch(arr,ele,start,end)
print(index)