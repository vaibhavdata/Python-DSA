from turtle import left


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root == None:
        return 0
    else:
        lh = height(root.left)
        rh = height(root.right)
        return max(lh, rh) + 1
root = Node(10)
root.left = Node(5)
root.left.right = Node(3)
root.left.left = Node(2)
root.left.left.left = Node(111)
root.right = Node(12)
root.right.right =Node(15)
root.right.left = Node(16)
print(height(root))

# secode method in python
class Solution:
    def height2(self,root):
        if root is None:
            return  
        l_height = self.height2(root.left)
        r_right = self.height2(root.right)
        return max(l_height,r_right) + 1