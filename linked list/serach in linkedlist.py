class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
def serachLinkedElement(head,x):
    curr = head
    pos = 1
    while curr != None:
        if curr.key ==x:
            return pos
        pos= pos +1
        curr = curr.next
    return -1

# driver code 

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
x =40
print(serachLinkedElement(head,x))