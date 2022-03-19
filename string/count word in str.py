def countwordnStr(s):
    count =1
    for i in s:
        if i in " ":
            count += 1
    return count
s = "geeks for geeks classes !"
print(countwordnStr(s))