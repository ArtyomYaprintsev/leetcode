import pytest

from solution import Solution


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.mark.parametrize(
    ["input_lst", "expected"],
    [
        ([0, 1], 0),
        ([1, 1], 1),
        ([1, 10], 1),
        ([1, 2, 3], 2),
        ([1, 1, 5, 5, 1], 5),
        ([5, 5, 1, 1, 1, 1, 1], 6),
        ([5, 1, 5], 10),
        ([5, 1, 1, 5], 15),
        ([1, 1, 1, 1, 1], 4),
        ([1, 1, 10, 1, 1], 4),
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1] + [0] * 10_000 + [1], 10_001),
    ],
)
def test_solution(solution: Solution, input_lst: list[int], expected: int):
    assert solution.maxArea(input_lst) == expected
