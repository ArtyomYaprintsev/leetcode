"""Problem: 605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are
not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty
and 1 means not empty, and an integer n, return true if n new flowers can be
planted in the flowerbed without violating the no-adjacent-flowers rule and
false otherwise.

Constraints:
    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length
"""


# The problem solution
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        possible_flowers = 0
        flowerbed_len = len(flowerbed)

        for index in range(flowerbed_len):
            before, cur, after = (
                flowerbed[index - 1] if index != 0 else 0,
                flowerbed[index],
                flowerbed[index + 1] if index != flowerbed_len - 1 else 0,
            )

            if before == 0 and cur == 0 and after == 0:
                possible_flowers += 1
                flowerbed[index] = 1

        return possible_flowers >= n
