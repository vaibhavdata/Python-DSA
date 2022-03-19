def insert_array_end(arr,ele):
    arr.append(ele)
    return arr
arr =[3,4,5,6,7]
ele =100
flag = insert_array_end(arr,ele)
print(flag)