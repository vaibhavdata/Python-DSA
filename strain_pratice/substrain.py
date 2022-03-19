def substring(s1,s2):
    m =  len(s1)
    n = len(s2)
    for i in range(n-m+1):
        for j in range(m):
            if s2[i+j] != s1[j]:
                break
    if (j+1)==m:
        return i
    return -1


s1 = "euro"
s2 = "ineuron"
flag = substring(s1,s2)
print(flag)
    