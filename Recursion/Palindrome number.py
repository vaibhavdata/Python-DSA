from pickletools import read_unicodestring1


op =0
def reversANumber(n):
    global op
    if n < 10:
        op = op*10 +n%10
        return 
    op = op*10 + n%10
    reversANumber(n//10)

    

n= 123
reversANumber(n)
if op==n:
    print("palindrome number")
else:
    print("no palindr number")
print()
op = 0
def reverseANumber(num):
    global op 
    if num<10:
       op=op*10+num%10 
       return
   
    op=op*10+num%10
    reverseANumber(num//10)

num = 3443
reverseANumber(num)

if op==num:
    print("Palindrome number")
else:
    print("Not a palindrome")