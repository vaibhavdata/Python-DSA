class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
def getceil(root,x):
    res = None
    while root !=None:
        if root.key ==x:
            return root
        elif root.right < x:
            root = root.right

        else:
            res = root
            root = root.left

    return res