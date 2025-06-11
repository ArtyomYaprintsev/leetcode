import pytest

from solution import Solution


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.mark.parametrize(
    ["input_lst", "expected_lst"],
    [
        ([0], [0]),
        ([1], [1]),
        ([0, 1], [1, 0]),
        ([1, 0], [1, 0]),
        ([0, 0, 1], [1, 0, 0]),
        ([1, 0, 1], [1, 1, 0]),
        ([1, 0, 2], [1, 2, 0]),
        ([0, 3, 2], [3, 2, 0]),
        ([2, 3, 1], [2, 3, 1]),
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ],
)
def test_solution(
    solution: Solution,
    input_lst: list[int],
    expected_lst: list[int],
):
    assert solution.moveZeroes(input_lst) == expected_lst
