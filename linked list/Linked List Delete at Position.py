class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def deletePostionLinkedList(head,pos):
    if head ==None:
        return None
    if pos ==1:
        return head.next
    curr = head
    for i in range(pos -2):
        curr=curr.next
        if curr == None:
            return head
    curr.next = curr.next.next
    return head
def insertPositionlinkedList(head,pos):
    if head ==None:
        return None
    if pos ==1:
        return head.next
    curr = head
    for i in range(pos -2):
        curr = curr.next
        if curr ==None:
            return head
    curr.next = curr.next.next
    return head

def printList(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next
    print()


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

printList(head)

head = deletePostionLinkedList(head,4)

printList(head)