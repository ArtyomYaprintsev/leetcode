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

        left = -1
        right = 0

        cur_zeros = int(nums[0] == 0)
        max_length = 0

        while right < len(nums) - 1:
            print(left, "-", right, "| zeros", cur_zeros)
            # print(
            #     "-" * 7,
            #     right - left + 1 if right != left or nums[right] == 1 else 0,
            # )

            # max_length = max(
            #     max_length,
            #     right - left + 1 if right != left or nums[right] == 1 else 0,
            # )

            if nums[right + 1] == 1:
                right += 1
                continue

            if cur_zeros < k:
                right += 1
                cur_zeros += 1
                continue

            left += 1

            if right == left - 1 and cur_zeros == 1:
                right += 1

            if nums[left] == 0:
                cur_zeros -= 1

        return max_length


if __name__ == "__main__":
    # print(Solution().longestOnes([0], 0))
    # print(Solution().longestOnes([0], 5))
    # print(Solution().longestOnes([1], 0))
    # print(Solution().longestOnes([1], 5))
    print(Solution().longestOnes([0, 0, 1], 1))
    # print(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
