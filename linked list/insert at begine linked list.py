class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
def insertbegine(head,key):
    temp = Node(key)
    temp.next = head
    return temp


# driver code 
head = None
head = insertbegine(head,10)
head = insertbegine(head,20)
head = insertbegine(head,30)

def printFuncation(head):
    curr = head
    while curr != None:
        print(curr.key,end =" ")
        curr = curr.next
printFuncation(head)