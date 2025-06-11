"""Problem: 392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false
otherwise.

A subsequence of a string is a new string that is formed from the original
string by deleting some (can be none) of the characters without disturbing
the relative positions of the remaining characters. (i.e., "ace" is a
subsequence of "abcde" while "aec" is not).

Constraints:
    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.
"""


# The problem solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        substr_i = 0
        str_i = 0

        while substr_i < len(s) and str_i < len(t):
            if s[substr_i] == t[str_i]:
                substr_i += 1
            str_i += 1

        return substr_i == len(s)


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
