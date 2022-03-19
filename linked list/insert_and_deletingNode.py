class Node:
    def __init__(self,data):
        self.val = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def insertIntoFirstNode(self,data):
        new_node = Node(data)
        new_node.start = self.head
        self.head = new_node
    def deleteFirstElement(self):
        if self.head ==None:
            return None
        else:
            self.head = self.head.next
    def print(self):
        cur = self.head
        while cur != None:
            print(cur.val,end=" ")
            cur = cur.next
        print()
l = Linkedlist()
node_value = [1,2,3,4,5,6,7]
for i in node_value:
    l.insertIntoFirstNode(i)
l.print()
l.deleteFirstElement()
l.print()
print()

class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self,data):
        newNode = Node(data)
        newNode.next  =self.head
        self.head = newNode

    def deleteAtStart(self):
        if self.head==None:
            return None 
        else:
            self.head = self.head.next

    def print(self):
        cur = self.head 
        while cur!=None:
            print(cur.val,end=" ")
            cur = cur.next
        print()

l = LinkedList()
nodes_val = [1,2,3,4,5]
for i in nodes_val:
    l.insertAtStart(i)

l.print()
l.deleteAtStart()
l.print()