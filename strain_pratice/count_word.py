def countwordnStr(s):
    count =1
    for i in s:
        if i in " ":
            count += 1
    return count
s = "geeks for geeks classes !"
print()
def count_word(s):
    count =1
    for i in s:
        if i in " ":
            count +=1
    return count
s = "hello gays !"
flag = count_word(s)
print(flag)
        
