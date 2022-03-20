def insert(root, Key):
    # code here
    if root ==None:
        return Node(Key)
    elif root.data ==Key:
        return root
    elif root.data >Key:
        root.left = insert(root.left,Key)
    else:
        root.right = insert(root.right,Key)
    return root