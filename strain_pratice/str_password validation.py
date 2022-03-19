import re
def passwordValidatio(s):
    first = len(s)>=10
    second = re.findall('[A-Z]',s)
    thired = re.findall('[a-z]',s)
    forth = re.findall('[\d]',s)
    five = re.findall('[\@\*\#\$\-]',s)
    if first and second and thired and forth and five:
        return 1
    
    else:
        return 0
s ="eHello123@"
print(passwordValidatio(s))