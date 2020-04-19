from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    seen = []
    while L:
        seen.append(L.data)
        L = L.next

    n = len(seen)

    for i in range(0, n//2):
        l, r = seen[i], seen[n-1-i]
        if l != r:
            return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
