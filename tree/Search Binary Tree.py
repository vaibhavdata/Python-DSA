class Node:
    def __init__(self,data):
        self.key =  data
        self.left = None
        self.right = None
def serach(root,key):
    if root is None:
        return False
    elif root.key ==key:
        return True
    elif serach(root.left,key):
        return True
    else:
        return (root.right,key)

root = Node(10)
root.left = Node(5)
root.left.right = Node(3)
root.left.left = Node(2)
root.right = Node(12)
root.right.right =Node(15)
root.right.left = Node(16)
print(serach(root,19))
