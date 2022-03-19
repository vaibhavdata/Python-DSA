def reverseArray(arr):
    i =0
    j = len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i +=1
        j -=1
    return arr
arr =[2,3,4,56,6,7,1]
flag = reverseArray(arr)
print(flag)

def reverseArray(self,n,arr):
        #code here
        stack=[]
        for i in range(0,n):
           stack.append(arr[i])
        j =0
        while stack !=[] and j<n:
            arr[j] =stack.pop()
            j +=1
        return arr

def reverseAnArray(ip_array):
    if len(ip_array)==1:
        return
    alpha = ip_array.pop(0)
    reverseAnArray(ip_array)
    ip_array.append(alpha)

ip_array = [1,2,3]
reverseAnArray(ip_array)
print(ip_array)