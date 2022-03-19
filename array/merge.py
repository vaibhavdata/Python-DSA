def merge(arr1,arr2):
    arr =[-1]*(len(arr1)+len(arr2))
    i =0
    j =0
    k =0
    while i<len(arr1) and j<len(arr2):
        arr[k]=arr[i]
        i+1
        k+=1
    else:
        arr[k] = arr2[j]
        j+=1
        k+=1 