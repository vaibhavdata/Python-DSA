def array_insert_index(arr,index,ele):
    arr.insert(index,ele)
    return arr
arr = [3,5,6,7,9,10]
index =4
ele = 8
flag = array_insert_index(arr,index,ele)
print(flag)