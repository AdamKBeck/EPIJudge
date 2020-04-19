from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    def tail(x):
        acc = 0
        last_seen = None
        while x:
            acc += 1
            last_seen = x
            x = x.next
        return acc, last_seen

    if not L or not L.next:
        return L

    n, end = tail(L)
    end.next = L  # connect the end with the start
    k %= n  # k can be much bigger than n, so we can reduce the unneeded iteration

    # iterate to our new end
    curr = L
    for _ in range(n-k-1):
        curr = curr.next

    new_head = curr.next
    curr.next = None
    return new_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))