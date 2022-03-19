class Node:
    def __init__(self,key):
        self.value = key
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
l =  LinkedList()
print(l.head)