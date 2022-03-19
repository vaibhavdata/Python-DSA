


class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
def insertatend(head,key):
    if head == None:
        return Node(key)
    curr =head
    while curr.next !=None:
        curr = curr.next
    curr.next = Node(key)
    return head


head = None
head = insertatend(head,10)
head =insertatend(head,20)
head = insertatend(head,30)
def printFuncation(head):
    curr = head
    while curr != None:
        print(curr.key,end=" ")
        curr = curr.next
printFuncation(head)