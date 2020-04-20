from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    copy = ans = ListNode()
    carry = 0

    while L1 or L2 or carry:
        val = (L1.data if L1 else 0) + (L2.data if L2 else 0) + carry
        carry = val // 10
        val %= 10

        ans.next = ListNode(val)
        ans = ans.next
        L1 = L1.next if L1 else L1
        L2 = L2.next if L2 else L2

    return copy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
