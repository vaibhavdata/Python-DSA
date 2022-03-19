op =0
def reverseANumber(n):
    global op
    if n<10:
        op = op*10 + n
        return 
    op = op*10+ n%10
    reverseANumber(n//10)
reverseANumber(3546)
print(op)
print()

# print 3456 as 6543 
op =0
def reversNumber(n):
    global op
    if n <10:
        op = op*10 + n
        return 
    op = op*10 + n%10
    reversNumber(n//10)
reversNumber(3456)
print(op)


