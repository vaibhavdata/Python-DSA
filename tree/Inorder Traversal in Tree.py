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
def inorder2(root):
    relist=[]
    if root is None:
        return relist
    inorderhelp2(root,relist)
    return root
def inorderhelp2(root,relist):
    if root == None:
        return 
    inorderhelp2(root.left,relist)
    relist.append(root.data)
    inorderhelp2(root.right,relist)
    return root

root = Node(10)
root.left= Node(5)
root.left.left = Node(8)
root.left.left.left = Node(9)
root.right =Node(12)
root.right.right= Node(14)

inorder(root)
print(inorder2(root))
