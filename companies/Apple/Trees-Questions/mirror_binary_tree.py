def mirror_binary_trees(root):
    if not root:
        return None

    root.right, root.left = root.left, root.right
    mirror_binary_trees(root.right)
    mirror_binary_trees(root.left)

    return root



