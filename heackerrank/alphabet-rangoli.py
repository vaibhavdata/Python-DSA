import re
n= int(input())
for i in range(n):
    try:
        re.compile(input())
        Output = True
    except re.error:
        Output = False
print(Output)