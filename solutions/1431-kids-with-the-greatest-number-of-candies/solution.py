"""Problem: 1431. Kids With the Greatest Number of Candies

There are n kids with candies. You are given an integer array candies, where
each candies[i] represents the number of candies the ith kid has, and an
integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after
giving the ith kid all the extraCandies, they will have the greatest number of
candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

Constraints:
    n == candies.length
    2 <= n <= 100
    1 <= candies[i] <= 100
    1 <= extraCandies <= 50
"""


# The problem solution
class Solution:
    def kidsWithCandies(
        self,
        candies: list[int],
        extra: int,
    ) -> list[bool]:
        if not candies:
            return []

        max_candies = max(candies)

        # return [
        #     candy + extra >= max_candies
        #     for candy in candies
        # ]

        return list(
            map(
                lambda candy: candy + extra >= max_candies,
                candies,
            ),
        )
