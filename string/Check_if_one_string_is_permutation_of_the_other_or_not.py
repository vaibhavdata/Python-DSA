def isPermutation1(str1,str2):
    str1= list(str1)
    str2= list(str2)
    str1.sort()
    str2.sort()
    if str1==str2:
        return True
    return False
str1 = "abc"
str2 ="bac"
flag = isPermutation1(str1,str2)
print(flag)
print("Second method ")

def isPermutation2(str1,str2):
    count = {}
    for i in str1:
        if i in count:
            count[i] =count[i]+1
        else:
            count[i] =1
    for j in str2:
        if j in count:
            count[j]= count[j]+1
        else:
            count[j] =1
    for i,j in count.items():
        if j!=0:
            return False
        return True
    return count
str1 = "abc"
str2 ="bacd"
flag = isPermutation2(str1,str2)
print(flag)