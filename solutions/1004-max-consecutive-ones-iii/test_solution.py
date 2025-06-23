import pytest

from solution import Solution


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.mark.parametrize(
    ["input_nums", "input_k", "output"],
    [
        ([0], 0, 0),
        ([1], 0, 1),
        ([1], 2, 1),
        ([0, 0], 0, 0),
        ([0, 0], 1, 1),
        ([0, 0], 2, 2),
        ([1, 0], 0, 1),
        ([1, 0], 1, 2),
        ([1, 0], 2, 2),
        ([1, 0, 1], 1, 3),
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
        ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
    ],
)
def test_solution(
    solution: Solution,
    input_nums: list[int],
    input_k: int,
    output: int,
):
    assert solution.longestOnes(input_nums, input_k) == output
