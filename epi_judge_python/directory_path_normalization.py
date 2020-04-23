from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    stack = []

    for x in path.split('/'):
        if not x or x == '.':
            continue
        elif x == '..':
            if stack and stack[-1] != '..':
                stack.pop()
            else:
                stack.append(x)
        else:
            stack.append(x)

    optional_start = '/' if path[0] == '/' else ''
    return optional_start + '/'.join(stack)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
