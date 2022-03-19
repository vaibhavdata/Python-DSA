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
def display(head):
    curr = head
    list1= []
    while curr != None:
        list1.append(curr.key)
        curr = curr.next
    return list1
head =Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
printList(head)
index=display(head)
print(index)
