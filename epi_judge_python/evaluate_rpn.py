from test_framework import generic_test


def evaluate(expression: str) -> int:
    stack = []
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: b - a,
        '*': lambda a, b: a * b,
        '/': lambda a, b: b // a,
    }

    for x in expression.split(','):
        if x in ops:
            stack.append(
                ops[x](stack.pop(), stack.pop())
            )
        else:
            stack.append(int(x))

    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
