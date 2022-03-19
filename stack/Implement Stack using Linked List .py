class Node:
    def __init__(self,data):
        self.data = data
        self.next =None
class Mystack:
    def __init__(self):
        self.head = None

    def push(self,data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
    def pop(self):
        if self.head is None:
            return -1
        ans_da = self.head.data
        self.head = self.head.next
        return ans_da
n = Node(10)
n.next = Node(20)
n.next.next = Node(30)
n.next.next.next = Node(40)
m = Mystack()

