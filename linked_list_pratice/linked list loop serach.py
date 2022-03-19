class Node:
    def __init__(self,key):
        self.key= key
        self.next = None
def checkloop(head):
    hash = {}
    loopnode = None
    curr =head
    while curr != None:
        if curr in hash:
            hash[curr]=True
        else:
            loopnode = curr
            break
    return loopnode
def printFuncation(head):
    curr = head
    while curr !=None:
        print(curr.key,end=" ")
        curr = curr.next
    print()

head =Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(4)
#printFuncation(head)
li = checkloop(head)
printFuncation(li)

