def merage_array(arr1,arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)
    return list(sorted(arr1.union(arr2)))
arr1 = [2,3,4,5,6,7]
arr2 =[5,6,7,8,3,9]
flag =merage_array(arr1,arr2)
print(flag)