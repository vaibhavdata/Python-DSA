class Node:
    def __init__(self,key):
        self.left =None
        self.right = None
        self.key = key
def getSucc(curr, key):
    while curr.left !=None:
        curr = curr.left
    return curr.key
def deleteNode(root,key):
    if root ==None:
        return
    if root.key >key:
        root.left = deleteNode(root.left,key)
    if root.key <key:
        root.right = deleteNode(root.right,key)
    else:
        if root.left ==None:
            return root.right
        elif root.right ==None:
            return root.left
        else:
            succes = getSucc(root.right,key)
            root.key = succes
            root.right = deleteNode(root.right, succes)
    return root

