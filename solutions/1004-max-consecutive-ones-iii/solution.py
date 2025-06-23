"""Problem: 1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of
consecutive 1's in the array if you can flip at most k 0's.

Constraints:
    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
    0 <= k <= nums.length
"""


# The problem solution
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return int(k > 0) or nums[0]

        left = 0
        right = 0

        # Zeros between `left` and `right` pointers
        cur_zeros = int(nums[0] == 0)
        max_length = 0

        while right < len(nums):
            max_length = max(
                max_length,
                right - left + (1 if nums[left] or k > 0 else 0),
            )

            if right == len(nums) - 1:
                break

            if nums[right + 1] == 1:
                right += 1
                continue

            if cur_zeros < k:
                right += 1
                cur_zeros += 1
                continue

            if nums[left] == 0:
                cur_zeros -= 1

            if left == right:
                right += 1

                if nums[right] == 0:
                    cur_zeros += 1

            left += 1

        return max_length
