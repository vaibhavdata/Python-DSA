from itertools import count


def anramstr(s1,s2):
    s2 = list(s2)
    s1 = list(s1)
    s1.sort()
    s2.sort()
    if s1 ==s2:
        return True
    else:
        return False
s1 = "abcd"
s2 ="dcba"
flag = anramstr(s1,s2)
print(flag)

# second method in str
def  isPermutation2(s1,s2):
    count1 = {}
    count2 = {}
    for i in s1:
        if i in count1:
            count1[i] =count1[i]+1
        else:
            count1[i]=1
    for i in s2:
        if i in count2:
            count2[i]=count2[i]+1
        else:
            count2[i]=1
    for i in list(set(s1+s2)):
        if i not in count1 or i not in count2 or count1[i] != count2[i]:
            return False
        else:
            return True
s1 = "abcd"
s2 ="dcba"
flag = isPermutation2(s1,s2)
print(flag)