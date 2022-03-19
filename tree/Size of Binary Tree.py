class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def size_of_binary(root):
    if root ==None:
        return 0
    else:
        lf = size_of_binary(root.left)
        rf = size_of_binary(root.right)
        return 1+lf+rf
root = Node(10)
root.left = Node(5)
root.left.right = Node(3)
root.left.left = Node(2)
root.right = Node(12)
root.right.right =Node(15)
root.right.left = Node(16)
print(size_of_binary(root))