class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

def insertbegine(head,a):
    temp=Node(a)
    if head==None:
        return temp
    temp.next=head
    return temp
def insertEndBegine(head,b):
    new= Node(b)
    if head == None:
        return new
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = new
    return head
def printList(head):
    curr = head
    while curr != None:
        print(curr.key,end=" ")
        curr = curr.next
    print()
        


head = Node(10)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(25)
a = 5
b= 50

insertbegine(head, a)
printList(head)
insertEndBegine(head, b)
printList(head)

