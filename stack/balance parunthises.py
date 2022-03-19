def matchingOrNot(a,b):
    if (a=='('  and b==')') or (a=='[' or b==']') or (a=='{' and b=='}'):
        return True
    else:
        return False
def is_Balanced(int):
    stack =[]
    for  i in int:
        if i in ('(','[',"{"):
            stack.append(i)
        else:
            if not stack:
                return False
            elif matchingOrNot(stack[-1],i)=='False':
                return False
            else:
                stack.pop()
                
    if stack:
        return False
    else:
        return True
input = '({{[[]}})'
print(is_Balanced(input))