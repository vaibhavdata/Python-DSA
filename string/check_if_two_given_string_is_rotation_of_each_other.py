def strRotationofEach(s1,s2):
    if len(s1) !=len(s2):
        return False
    temp = s1 + s2
    if s2 in temp:
        return True
    else:
        return False
s1 ='abcd'
s2 = 'dcba'
op =strRotationofEach(s1,s2)
print(op)
