class Node:
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None
def insert(root,key):
    present = None
    curr = root
    while curr !=None:
        present = curr
        if curr.key ==None:
            return root
        elif curr.key < key:
            curr = curr.left
        else:
            curr = curr.right
    if present == None:
        return Node(key)

    if present.key > key:
        present.left = Node(key)
    else:
        present.right = Node(key)

    return root