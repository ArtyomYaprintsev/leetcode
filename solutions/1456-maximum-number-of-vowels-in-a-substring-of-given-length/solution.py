"""Problem: 1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters
in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Constraints:
    1 <= s.length <= 10^5
    s consists of lowercase English letters.
    1 <= k <= s.length
"""


# The problem solution
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        cur_vowels = 0

        for i in range(k):
            if s[i] in vowels:
                cur_vowels += 1

        max_vowels = cur_vowels

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                cur_vowels -= 1

            if s[i] in vowels:
                cur_vowels += 1

            if cur_vowels > max_vowels:
                max_vowels = cur_vowels

        return max_vowels
