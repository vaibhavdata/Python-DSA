def checkpallindrome(ip_str):
    n = len(ip_str)
    i =0
    j = len(ip_str)-1
    while i<j:
        if ip_str[i] !=ip_str[j]:
            return False
        i +=1
        j -=1
    return True
ip_str = "abcba"
flag = checkpallindrome(ip_str)
print(flag)