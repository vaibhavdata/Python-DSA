class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
def printList(head):
    curr = head
    while curr !=None:
        print(curr.key,end=" ")
        curr = curr.next
    #print()
def sum_of_element(head):
    curr = head
    sum = 0
    while curr !=None:
        sum += curr.key
        curr = curr.next
    return sum
head = Node(10)
head.next = Node(20)
head.next.next = Node(40)
head.next.next.next = Node(60)
printList(head)
print()
index =sum_of_element(head)
print(index)

#printList(head)
