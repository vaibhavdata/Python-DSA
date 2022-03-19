n= int(input())
s = set(map(int,input().split()))
num = int(input())
for i in range(num):
    print(i)
    ip = input().split()
    print(ip)
    if ip[0]=="remove":
        s.remove(int(ip[1]))
    elif ip[0]=="discard":
        s.discard(int(ip[1]))
    else:
        s.pop()
print(sum(s))
