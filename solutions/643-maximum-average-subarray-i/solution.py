"""Problem: 643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum
average value and return this value. Any answer with a calculation error less
than 10-5 will be accepted.

Constraints:
    n == nums.length
    1 <= k <= n <= 10^5
    -10^4 <= nums[i] <= 10^4
"""


# The problem solution
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cur_sum: int = nums[0]

        for i in range(1, k):
            cur_sum += nums[i]

        max_sum = cur_sum

        for i in range(k, len(nums)):
            cur_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, cur_sum)

        return max_sum / k
