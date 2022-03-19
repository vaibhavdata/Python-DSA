class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def joinTwoList(head1,head2):
    if (head1==None and head2==None):
        return None
    if head1 ==None:
        return head2
    if head2 ==None:
        return head1
    curr = head1
    while curr.next !=None:
        curr = curr.next
    curr.next = head2
    return head1


def printList(head1,head2):
    curr = head1
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next
    print()


head1 = Node(10)
head1.next = Node(20)


head2 = Node(5)
head2.next = Node(15)
head2.next.next = Node(25)

printList(head1,head2)

joinTwoList(head1,head2)

printList(head1,head2)