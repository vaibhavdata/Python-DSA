def checkgivenpallindrome(ip_str):
    i=0
    j = len(ip_str)-1
    while i<j:
        if ip_str[i] !=ip_str[j]:
            return False
        i +=1
        j -=1
    return True
ip_str = 'abcbad'
op = checkgivenpallindrome(ip_str)
print(op)
    
