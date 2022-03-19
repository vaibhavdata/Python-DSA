def zerotoOne(arr):
    i = 0
    j = len(arr)-1
    while i<j:
        if arr[i]==0:
            arr[i],arr[j]=arr[j],arr[i]
            j -=1
        else:
            i +=1
arr = [-5,0,1,0,4,-0,-7,8,9,10]
zerotoOne(arr)
print(arr)