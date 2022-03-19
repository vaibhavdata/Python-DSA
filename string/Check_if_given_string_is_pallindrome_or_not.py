from audioop import reverse


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
print("Seconde method ")
# seconde method checkgivenpallindrome
def reverse(ip_str):
    ip_str = list(ip_str)
    i =0
    j = len(ip_str)-1
    while i<j:
        ip_str[i],ip_str[j]=ip_str[j],ip_str[i]
        i +=1
        j -=1
    ip_str ="".join(ip_str)
    return ip_str
def checkPal1(ip_str):
    reverse_ip = reverse(ip_str)
    if reverse_ip==ip_str:
        return True
    return False
ip_str = 'abcba'
op = checkgivenpallindrome(ip_str)
print(op)    
