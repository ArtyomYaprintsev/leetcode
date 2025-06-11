"""Problem: 11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints:
    n == height.length
    2 <= n <= 10^5
    0 <= height[i] <= 10^4
"""


# The problem solution
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left_i = 0
        right_i = len(height) - 1

        area = 0

        while left_i < right_i:
            area = max(
                (right_i - left_i) * min(height[left_i], height[right_i]),
                area,
            )

            if height[left_i] > height[right_i]:
                right_i -= 1
            else:
                left_i += 1

        return area
