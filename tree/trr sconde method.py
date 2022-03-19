class Tree:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

root = Tree(10)
root.left = Tree(20)
root.right =Tree(30)
root.left.left = Tree(40)
root.left.left.left =Tree
print(root())