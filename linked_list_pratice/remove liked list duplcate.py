
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
def printFuncation(head):
    curr = head
    while curr != None:
        print(curr.data,end = " ")
        curr = curr.next
    print()

def removedubplicated(head):
    curr = head
    while curr.next !=None:
        if curr.data ==curr.next.data :
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(30)
head.next.next.next.next = Node(40)
printFuncation(head)
removedubplicated(head)
printFuncation(head)