class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None
class BinarySerachTree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        if self.root ==None:
            self.root = Node(data)
        else:
            cur = self.root
            while 1:
                if data <cur.val:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = Node(data)
                        break
                elif data >cur.val:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right =Node(data)
                        break
                else:
                    break
tree = BinarySerachTree()
nodes = [6,8,7,9,4,3,5]
for i in nodes:
    tree.insert(i)

print(tree.root.val)          
