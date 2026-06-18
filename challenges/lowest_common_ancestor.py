from data_structures.node import Node


def lowest_common_ancestor(
    root: Node | None,
    value1: int,
    value2: int,
) -> int:
    current = root

    while current is not None:
        if value1 < current.value and value2 < current.value:
            current = current.left

        elif value1 > current.value and value2 > current.value:
            current = current.right

        else:
            return current.value
