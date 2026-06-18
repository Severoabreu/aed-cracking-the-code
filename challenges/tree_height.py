from data_structures.node import Node


def tree_height(root: Node | None) -> int:
    if root is None:
        return -1
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    return 1 + max(left_height, right_height)
