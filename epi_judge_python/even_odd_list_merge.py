from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    odd_head, even_head = ListNode(), ListNode()
    odd_last, even_last = odd_head, even_head

    is_even = True
    while L:
        if is_even:
            even_last.next = L
            even_last = L
        else:
            odd_last.next = L
            odd_last = L

        L = L.next
        is_even = not is_even

    even_last.next = odd_head.next
    odd_last.next = None
    return even_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge)
    )