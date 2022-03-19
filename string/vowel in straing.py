def countvowel(s):
    count = 0
    for i in s:
        if i in 'aeiou':
            count +=1
    return count
s = "gEEeksforgeeks"
print(countvowel(s))

# if we have caplital alppha
def is_vowal(s):
    return s.upper() in ['A', 'E', 'I', 'O', 'U']
def countvowel(s):
    count =0
    for i in range(len(s)):
        if is_vowal(str[i]):
            count +=1
    return count
    