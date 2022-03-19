from math import inf

class  Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def maximum_in_binary(root):
    if root ==None:
        return -inf
    else:
        lm = maximum_in_binary(root.left)
        rm = maximum_in_binary(root.right)
        return max(root.data,lm,rm)
root = Node(10)
root.left = Node(5)
root.left.right = Node(3)
root.left.left = Node(2)
root.right = Node(12)
root.right.right =Node(15)
root.right.left = Node(16)
print(maximum_in_binary(root))