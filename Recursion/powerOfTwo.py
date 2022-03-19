def powerOfTwo(n):
    if n==0:
        return 1
    elif n%2==0:
        return  powerOfTwo(n//2)*powerOfTwo(n//2)
    else:
        return 2*powerOfTwo(n//2)*powerOfTwo(n//2)

print(powerOfTwo(7))

# second method 
def poweroftwo(n):
    if n==0:
        return 1
    elif n%2==0:
        return poweroftwo(n//2)*poweroftwo(n//2)
    else:
        return 2*poweroftwo(n//2)*poweroftwo(n//2)
print(poweroftwo(7))