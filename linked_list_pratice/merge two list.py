class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
def printFuncation(head):
    curr = head
    while curr != None:
        print(curr.data,end = " ")
        curr = curr.next
    print()
def mergetolist(head1,head2):
    if (head1== None and head2==None):
        return None
    if head1==None:
        return head2
    if head2 ==None:
        return None
    curr = head1
    while curr.next !=None:
        curr = curr.next
    curr.next =head2
    return head1


head1 = Node(10)


head2 = Node(5)
head2.next = Node(15)
head2.next.next = Node(25)
#printFuncation(head1)
merge = mergetolist(head1,head2)
printFuncation(merge)
