class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
def insert_a_position(head,key,pos):
    temp = Node(key)

    if pos ==1:
        temp.next = head
        return temp
    curr = head

    for i in range(pos-2):
        curr = curr.next
        if curr == None:
            return head

    temp.next = curr.next
    curr.next = temp

    return head

def printFuncation(head):
    curr = head
    while curr != None:
        print(curr.key,end=" ")
        curr = curr.next
    print()
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

printFuncation(head)

insert_a_position(head,40,4)
printFuncation(head)
print()

def insert_a_postion_01(head,pos,key):
    temp = Node(key)
    if pos ==1:
        temp.next =head
        return temp
    curr = head
    for i in range(pos-2):
        curr =curr.next
        if curr == None:
            return head
    temp.next = curr.next
    curr.next = head
    return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(80)
head.next.next.next.next = Node(90)

printFuncation(head)

insert_a_postion_01(head,70,4)
printFuncation(head)