from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        curr  = {beginWord}
        end = {endWord}
        acc = 1

        if endWord not in words:
            return 0

        while curr and end and curr.isdisjoint(end):
            curr_next_words = set()
            end_next_words = set()

            words -= curr
            words -= end

            for x in curr:
                curr_next_words.update(find_next_words(x, words))

            for x in end:
                end_next_words.update(find_next_words(x, words))

            curr = curr_next_words
            end = end_next_words
            acc += 2

        return acc if curr and end else 0


def find_next_words(word, allowed_words):
    next_words = set()

    for x in allowed_words:
        if word_diff(word, x) == 1:
            next_words.add(x)

    return next_words


def word_diff(a, b):
    acc = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            acc += 1

    return acc


if __name__ == '__main__':
    s = Solution()
    l = s.ladderLength(
        "hit",
        "cog",
        ["hot","dot","dog","lot","log"],
    )
    print(l)
