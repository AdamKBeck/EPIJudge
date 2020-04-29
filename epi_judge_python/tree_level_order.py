from collections import deque
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []

    ans = []
    current_level = [tree]

    while current_level:
        current_vals = []
        next_level = []

        for x in current_level:
            current_vals.append(x.data)

            if x.left:
                next_level.append(x.left)
            if x.right:
                next_level.append(x.right)

        ans.append(current_vals)
        current_level = next_level

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
