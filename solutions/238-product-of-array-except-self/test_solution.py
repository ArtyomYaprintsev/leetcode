import pytest

from solution import Solution


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.mark.parametrize(
    ["input_lst", "expected_lst"],
    [
        ([1, 1], [1, 1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [6, 3, 2]),
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([-1, 1, 1, -3, 3], [-9, 9, 9, -3, 3]),
        ([0, 0, 10, 10], [0, 0, 0, 0]),
    ],
)
def test_solution(
    solution: Solution,
    input_lst: list[int],
    expected_lst: list[int],
):
    assert solution.productExceptSelf(input_lst) == expected_lst
