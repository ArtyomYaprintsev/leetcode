"""Problem: 1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k
and remove them from the array.

Return the maximum number of operations you can perform on the array.

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    1 <= k <= 10^9
"""


# The problem solution
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        operations = 0

        hash_map: dict[int, int] = {}

        for num in nums:
            remainder = k - num

            if remainder <= 0:
                continue

            if remainder in hash_map and hash_map[remainder] > 0:
                operations += 1
                hash_map[remainder] -= 1
            else:
                hash_map[num] = hash_map.get(num, 0) + 1

        return operations


if __name__ == "__main__":
    print(Solution().maxOperations([1, 1, 1, 2, 2, 2], 3))
