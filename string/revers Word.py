def reverseWord(S):
    newStr = ""
    arr = S.split(".")
    arr.reverse()
    l = len(arr)
    for i in range(l):
        if (i==l-1):
            newStr = newStr + arr[i]
        else:
            newStr = newStr +arr[i]+"."
    return newStr
S= "i.like.this.program.very.much"
flag = reverseWord(S)
print(flag)
