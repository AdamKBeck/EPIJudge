from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if L is None or L.next is None:
        return L

    dummy = curr = ListNode(next=L)

    # iterate to right before the start
    for _ in range(1, start):
        curr = curr.next

    a, b = curr, curr.next
    for _ in range(start, finish+1):
        c = b.next
        b.next = a
        a, b = b, c

    curr.next.next = b
    curr.next = a

    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
