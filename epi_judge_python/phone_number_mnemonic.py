from typing import List

from test_framework import generic_test, test_utils


DIGIT_TO_LETTERS = {
    0: ['0'],
    1: ['1'],
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z'],
}


def phone_mnemonic(phone_number: str) -> List[str]:
    if not phone_number:
        return ['']

    letters = DIGIT_TO_LETTERS[int(phone_number[0])]
    rest = phone_mnemonic(phone_number[1:])

    ans = []
    for x in letters:
        for word in rest:
            ans.append(x + word)

    return ans or ['']


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))