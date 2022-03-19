def middeleOFStack(n,stack):
    if n%2 ==0:
        mid = (1+n)/2
    else:
        mid = (1+n)//2
    for i in range(0,len(stack)):
        if i<mid:
            element = stack[i]
    return element

stack =[1,2,3,4]
print(middeleOFStack(4,stack))