class Node:
    def __init__(self,key):
        self.key = key
        self.next = None


def printList(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next
    print()
def maximum(head):
    curr = head
    t = curr.key
    while curr != None:
        if (t< curr.key):
            t = curr.key
    return t

def minimum(head):
    curr = head
    t = curr.key
    while curr != None:
        if (t>curr.key):
            t = curr.key
    return t


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

printList(head)

max = maximum(head)

print(max)
min = minimum(head)
print(min)