class Node:
    def __init__(self,key):
        self.key = key
        self.next =  None
def printList(head):
    curr = head
    while curr != None:
        print(curr.key,end=" ")
        break
        
        
        
def serach_linked(head,val):
    curr = head
    find_serach = None
    while curr != None:
        if curr.key ==val:
            find_serach = curr
            break
        curr = curr.next
    return find_serach




head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


flag=serach_linked(head,40)
printList(flag)