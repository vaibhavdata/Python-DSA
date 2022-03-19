def subarrayWith(arr,n):
    s = set([])
    sum = 0
    for i in range(n):
        sum += arr[i]
        if sum in s:
            return True
        if sum==0:
            return True
        s.add(sum)
    return False
arr =[2,5,-4,0]
n =4
flag = subarrayWith(arr,n)
print(flag)

        
