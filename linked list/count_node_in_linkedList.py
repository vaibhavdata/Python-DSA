class Node:
    def __init__(self, data):
        self.data =data
        self.next = None

def countNode(head):
    curr = head
    count = 0
    while curr != None:
        count +=1
        curr = curr.next
    return count



def printList(head):
    curr = head
    while curr !=None:
        print(curr.data,end=" ")
        curr = curr.next


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

printList(head)

head = countNode(head)

printList(head)