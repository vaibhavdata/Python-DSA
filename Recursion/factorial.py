# factorial iteration method
def factorial_iter(n):
    fact = 1
    for i in range(n,0,-1):
        fact = fact*i
    return fact

print(factorial_iter(5))
print()
# second method recursion 
def factorial_recursion(n):
    if n ==1:
        return 1
    else:
        return n*factorial_recursion(n-1)
print(factorial_recursion(12))