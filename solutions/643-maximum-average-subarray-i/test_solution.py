import pytest

from solution import Solution


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.mark.parametrize(
    ["input_lst", "input_k", "expected"],
    [
        ([1], 1, 1.0),
        ([1, 2], 2, 1.5),
        ([-1, 2], 2, 0.5),
        ([5], 1, 5.00000),
        ([-1, -2, -3, -4, -5, -100], 2, -1.5),
        ([-1, -2, -3, -4, -5, 100], 2, 47.5),
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
    ],
)
def test_solution(
    solution: Solution,
    input_lst: list[int],
    input_k: int,
    expected: float,
):
    assert solution.findMaxAverage(input_lst, input_k) == expected
