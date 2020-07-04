from collections import deque

from test_framework import generic_test
from test_framework.test_failure import TestFailure

class QueueWithMax:
    def __init__(self):
        self.Q = deque()
        self.max_Q = deque()

    def enqueue(self, x: int) -> None:
        self.Q.append(x)

        while self.max_Q and self.max_Q[-1] < x:
            self.max_Q.pop()

        self.max_Q.append(x)

    def dequeue(self) -> int:
        result = self.Q.popleft()

        if self.max_Q[0] == result:
            self.max_Q.popleft()

        return result

    def max(self) -> int:
        return self.max_Q[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
