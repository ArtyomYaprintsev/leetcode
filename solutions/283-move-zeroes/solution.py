"""Problem: 283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Constraints:
    1 <= nums.length <= 104
    -2^31 <= nums[i] <= 2^31 - 1
"""


# The problem solution
class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        zero_pointer = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_pointer] = nums[i]

                if zero_pointer != i:
                    nums[i] = 0

                zero_pointer += 1

        return nums


if __name__ == "__main__":
    print(Solution().moveZeroes([0, 1, 0, 3, 12]))
