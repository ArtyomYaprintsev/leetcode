"""Problem: 1768. Merge Strings Alternately.

You are given two strings word1 and word2. Merge the strings by adding letters
in alternating order, starting with word1. If a string is longer than the
other, append the additional letters onto the end of the merged string.

Return the merged string.

Constraints:
    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.
"""

from typing import Iterable


class Solution:
    def convertToGenerator(self, word1: str, word2: str) -> Iterable:
        len1 = len(word1)
        len2 = len(word2)

        index = 0

        while index < len1 or index < len2:
            if index < len1:
                yield word1[index]
            if index < len2:
                yield word2[index]
            index += 1

    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(self.convertToGenerator(word1, word2))
