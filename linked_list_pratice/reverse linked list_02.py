class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
def reverslinked(curr,pre =None):
    if curr == None:
        return pre
    next = curr.next
    curr.next = pre
    return reverslinked(curr,next)
def printList(head):
    curr = head
    while curr != None:
        print(curr.key,end=" ")
        curr = curr.next
    print()
head =Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
printList(head)

head = reverslinked(head)

printList(head)
