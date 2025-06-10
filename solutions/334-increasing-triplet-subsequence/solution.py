"""Problem: 334. Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices
(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
indices exists, return false.

Constraints:
    1 <= nums.length <= 5 * 105
    -2^31 <= nums[i] <= 2^31 - 1
"""


# The problem solution
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False

        i_first = 0
        i_second = 1
        i_third = 2

        while True:
            print(i_first, i_second, i_third)

            if nums[i_first] < nums[i_second] < nums[i_third]:
                return True

            if i_third < len(nums) - 1:
                i_third += 1

            if i_second < len(nums) - 2 and nums[i_second] >= nums[i_third]:
                i_second += 1

            if i_first == len(nums) - 3:
                break

            # if nums[i_first] >= nums[i_second]:
            i_first += 1

            if i_first == i_second:
                i_second += 1

        return False


if __name__ == "__main__":
    print(Solution().increasingTriplet([1, 2, 2, 1]))
    # print(Solution().increasingTriplet([2, 1, 5, 0, 4, 6]))
    # print(Solution().increasingTriplet([20, 100, 10, 12, 5, 13]))
    # print(Solution().increasingTriplet([0, 4, 2, 1, 0, -1, -3]))
