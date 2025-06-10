import pytest

from solution import Solution


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.mark.parametrize(
    ["input_lst", "expected"],
    [
        ([1], False),
        ([1, 2], False),
        ([1, 2, 3], True),
        ([1, 3, 2], False),
        ([1, 1, 1], False),
        ([1, 1, 1, 1], False),
        ([1, 2, 2, 1], False),
        ([1, 2, 3, 4], True),
        ([1, 2, 4, 3], True),
        ([4, 3, 2, 1], False),
        ([2, 1, 5, 0, 4, 6], True),
        ([20, 100, 10, 12, 5, 13], True),
        ([20, 10, 4, 100, 12, 5, 13], True),
        ([20, 10, 4, 100, 12, 5, 13, 101], True),
        ([0, 4, 2, 1, 0, -1, -3], False),
    ],
)
def test_solution(solution: Solution, input_lst: list[int], expected: bool):
    assert solution.increasingTriplet(input_lst) == expected
