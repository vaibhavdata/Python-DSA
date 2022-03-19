import re
def strvalidation(s):
    first = len(s)>=10
    second = re.findall("[\d]",s)
    third = re.findall("[A-Z]",s)
    forth=re.findall("[a-z]",s)
    five=re.findall("[\@\#\$\-\*]",s)
    if first and second and third and forth and five:
        return 1
    else:
        return 0
s ="eHello123@"
print(strvalidation(s))