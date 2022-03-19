def count_vowel(s):
    count =0
    for i in s:
        if i in 'aeiouAEIOU':
            count +=1
    return count
s ="geeksforGEEks"
flag = count_vowel(s)
print(flag)

