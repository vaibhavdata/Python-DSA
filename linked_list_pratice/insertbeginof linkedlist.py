class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
def insertbegin(head,key):
    temp =Node(key)
    temp.next = head
    return temp
def printFuncation(head):
    curr = head
    while curr != None:
        print(curr.key,end=" ")
        curr = curr.next

head = None
head = insertbegin(head,10)
head = insertbegin(head,20)
head = insertbegin(head,30)
printFuncation(head)