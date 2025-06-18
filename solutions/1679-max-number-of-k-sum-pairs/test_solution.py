import pytest

from solution import Solution


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.mark.parametrize(
    ["input_lst", "input_value", "output"],
    [
        ([1], 1, 0),
        ([1], 10, 0),
        ([1, 2], 2, 0),
        ([1, 2], 3, 1),
        ([1, 2, 3, 4], 5, 2),
        ([3, 1, 3, 4, 3], 6, 1),
        ([1, 1, 1, 2, 2, 2], 3, 3),
        ([2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3, 4),
    ],
)
def test_solution(
    solution: Solution,
    input_lst: list[int],
    input_value: int,
    output: int,
):
    assert solution.maxOperations(input_lst, input_value) == output
