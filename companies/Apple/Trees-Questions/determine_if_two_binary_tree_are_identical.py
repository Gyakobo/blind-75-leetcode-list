def same_trees(p, q) -> bool: # This is a recursive function
    # Takes care of both of them
    if not p and not q:
        return True

    # Stipulates whether one of the pointers was irregular
    if not p or not q or p.value != q.value:
        return False

    return (same_trees(p.left, q.left) and same_trees(p.right, q.right))

same_trees(btree, btree)