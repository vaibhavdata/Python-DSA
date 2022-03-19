class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
def delitefirst(head):
    if head ==None:
        return None
    else:
        return head.next
def printFuncaation(head):
    curr = head
    while curr !=None:
        print(curr.key,end=" ")
        curr = curr.next
    print()
head =Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
printFuncaation(head)
head =delitefirst(head)
printFuncaation(head)

