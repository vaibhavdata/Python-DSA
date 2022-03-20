from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def orderTra(self,root):
        res =[]
        stack = deque()
        if root ==None:
            return res
        else:
            stack.append(root)
        while len(stack) >0:
            node = stack.popleft()
            res.append(node.val)
            if node.left != None:
                stack.append(node.left)
        #check right
            if node.right != None:
                stack.append(node.right)
        return res

