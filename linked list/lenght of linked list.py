class Node:
    def __init__(self,key):
        self.key = key
        self.next =  None
def printList(head):
    curr = head
    while curr != None:
        print(curr)
        break
        
    
def lenghrList(head):
    if head ==None:
        return 0
    else:
        return 1+ lenghrList(head.next)
def lenghtlist2(head):
    curr = head
    len = 0
    while curr != None:
        len +=1
        curr = curr.next
    return len

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


flag=lenghrList(head)
printList(flag)
flag = lenghtlist2(head)
printList(flag)