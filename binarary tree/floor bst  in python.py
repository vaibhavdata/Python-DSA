class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
def getFloor(root,key):
    res = None
    while root !=None:
        if root.key ==None:
            return root
        elif root.key > key:
            root = root.left
        else:
            
            res = root
            root = root.right
    return root