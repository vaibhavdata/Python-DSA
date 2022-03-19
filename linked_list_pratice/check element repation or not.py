class Node:
    def __init__(self,key):
        self.key = key
        self.next =None
def printList(head):
    curr = head
    while curr !=None:
        print(curr.key,end=" ")
        curr = curr.next
    print()
def checkelementrepation(head):
    curr1 = head
    flag= False
    while curr1 != None:
        curr2 =head
        while curr2 !=None:
            if curr1==curr2 or curr1.key==curr2.key:
                flag = True
                break
            curr2 = curr2.next
        curr1 = curr1.next
    return flag
head= Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(30)
printList(head)
checkelementrepation(head)
printList(head)