def liner_serch(arr,ele):
    ind = -1
    for i in range(0,len(arr)):
        if arr[i]==ele:
            ind = i
            break
    
    return ind
    

arr = [4,5,0,3,1,6]
ele = 8
index = liner_serch(arr,ele)
print(index)

#here time and space complitive will be 0(n) and space compli will be 0(1)