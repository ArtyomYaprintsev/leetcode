"""Problem: 151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will
be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between
two words. The returned string should only have a single space separating the
words. Do not include any extra spaces.

Constraints:
    1 <= s.length <= 104
    s contains English letters (upper-case and lower-case), digits, and spaces ' '.
    There is at least one word in s.
"""


# The problem solution
class Solution:
    # def reverseWords(self, s: str) -> str:
    #     return " ".join(c for c in s.split(" ")[::-1] if c != "")

    def reverseWords(self, s: str) -> str:
        words: list[str] = []
        word: list[str] = []

        for char in s:
            if char == " ":
                if word:
                    words.append("".join(word))
                    word = []
                continue

            word.append(char)

        if word:
            words.append("".join(word))

        return " ".join(words[::-1])
