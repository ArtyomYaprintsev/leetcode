"""Problem: 345. Reverse Vowels of a String

Description.
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
and upper cases, more than once.

Constraints:
    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.
"""

VOWELS = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}


# The problem solution
class Solution:
    def reverseVowels(self, s: str) -> str:
        new_s: list[str] = []

        ptr = 0
        vowel_pointer = len(s) - 1

        while ptr < len(s):
            if s[ptr] in VOWELS:
                while not s[vowel_pointer] in VOWELS:
                    vowel_pointer -= 1
                new_s.append(s[vowel_pointer])
                vowel_pointer -= 1
            else:
                new_s.append(s[ptr])

            ptr += 1

        return "".join(new_s)


if __name__ == "__main__":
    print(Solution().reverseVowels("hello"))
