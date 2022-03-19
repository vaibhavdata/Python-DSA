class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Mystack:
    def __init__(self):
        self.head =None
        self.s = 0

    def push(self,data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        self.s = self.s +1
    def size(self):
        return self.s
    def peek(self):
        if self.head ==None:
            return -1

        return self.head.data
    def pop(self):
        if self.head ==None:
            return -1
        res = self.head
        self.head = self.head.next 
        self.s = self.s -1
        return res


s=Mystack() 
s.push(10)

s.push(20)
s.push(30)
s.push(40)
print(s.peek())
s.pop()
s.pop()
print(s.peek())
print(s.size())
