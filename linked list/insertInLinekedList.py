class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insertIntostart(self,data):
        new_node = Node(data)
        new_node.start = self.head
        self.head = new_node
l = LinkedList()
node_value = [1,2,3,4,5,6]
for i in node_value:
    l.insertIntostart(i)
print(l.head.val)