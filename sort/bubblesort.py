# sorting basically array 
#sort array two type ascending and descending arraybblesort
def bubblesort(arr):
    for  i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
arr = [5,1,2,3,4]
bubblesort(arr)
print(*arr)
print()
def bubleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] >arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr = [4,7,1,8,9,2,5,7,0]
bubleSort(arr)
print(*arr)

