"""Problem: 238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.

Constraints:
    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The input is generated such that answer[i] is guaranteed to fit in a
        32-bit integer.
"""

from functools import reduce


# The problem solution
class Solution:
    # def productExceptSelf(self, nums: list[int]) -> list[int]:
    #     zeros_count = sum(bool(num == 0) for num in nums)
    #     total = reduce(lambda cur, num: cur * (num or 1), nums, 1)

    #     for i in range(len(nums)):
    #         if zeros_count >= 2:
    #             nums[i] = 0
    #             continue

    #         if zeros_count and nums[i] != 0:
    #             nums[i] = 0
    #             continue

    #         nums[i] = total // (nums[i] or 1)

    #     return nums

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zeros_count = sum(bool(num == 0) for num in nums)
        total = reduce(lambda cur, num: cur * (num or 1), nums, 1)

        if zeros_count >= 2:
            return [0] * len(nums)

        if zeros_count:
            return [total if num == 0 else 0 for num in nums]

        return [total // num for num in nums]
