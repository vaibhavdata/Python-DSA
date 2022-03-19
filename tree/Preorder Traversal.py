class Node:
    def __init__(self,data):
        self.data= data
        self.left = None
        self.right = None
def preorder(root):
    if root != None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
root = Node(10)
root.left = Node(5)
root.left.right = Node(3)
root.left.left = Node(2)
root.right = Node(12)
root.right.right =Node(15)
root.right.left = Node(16)
preorder(root)
