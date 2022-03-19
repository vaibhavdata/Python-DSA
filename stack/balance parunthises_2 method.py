class Sotution:
    def ismatch(self,x):
        stack =[]
        for i in x:
            if i in ('{','(','['):
                stack.append(i)
            else:
                if len(stack)>0:
                    if i==']' and stack[-1]=='[':
                        stack.pop(-1)
                    elif i==')' and stack[-1]=='(':
                        stack.pop(-1)
                    elif i=='}' and stack[-1]=='{':
                        stack.pop(-1)
                    else:
                        stack.append(i)
        if len(stack)==0:
            return True
        else:
            return False
s = Sotution()
input = '({[]})'
print(s.ismatch(input))