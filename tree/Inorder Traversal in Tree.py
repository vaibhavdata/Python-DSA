from turtle import left


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

root = Node(10)
root.left= Node(5)
root.left.left = Node(8)
root.left.left.left = Node(9)
root.right =Node(12)
root.right.right= Node(14)

inorder(root)