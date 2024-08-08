"""Problem: 1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if
s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x
divides both str1 and str2.

Constraints:
    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.
"""

from math import gcd


# The problem solution
class Solution:
    def _get_gcd(self, *integers) -> int:
        if 0 in integers:
            return 0

        return gcd(*integers)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''

        return str1[:self._get_gcd(len(str1), len(str2))]
