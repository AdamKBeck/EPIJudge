from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    def list_len(x: ListNode) -> int:
        acc = 0
        while x:
            acc += 1
            x = x.next
        return acc

    dummy = ListNode(next=L)
    copy = dummy
    n = list_len(dummy)

    for _ in range(n-k-1):
        dummy = dummy.next

    dummy.next = dummy.next.next
    return copy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
