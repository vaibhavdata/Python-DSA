def word_maxFre(s):
    s = s.split()
    count = {}
    for i in s:
        if i in count:
            count[i] = count[i]+1
        else:
            count[i] =1

    maxvalue = -1
    ans =""
    for k,v in count.items():
        if v>maxvalue:
            maxvalue = v
            ans  = k + " "+str(v)
    return ans
s = "geeks for geeks in python in this in "
flag = word_maxFre(s)
print(flag)