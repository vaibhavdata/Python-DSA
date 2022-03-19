class Stack:
    def __init__(self):
        self.set =[]
    def push(self,data):
        self.set.append(data)
    def pop(self):
        popEle = -1
        if len(self.set)>0:
            popEle=self.set.pop(-1)
        return popEle
    def printall(self):
        for i in range(len(self.set)-1,-1,-1):
            print(i,end=" ")
        print()

s = Stack()
values = [1,2,3,4,5]
for i in values:
    s.push(i)
s.printall()
print(s.pop())
print(s.pop())
print(s.pop())
s.printall()
