import pytest

from solution import Solution


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.mark.parametrize(
    [
        "flowerbed",
        "n",
        "expected_result",
    ],
    [
        [[0], 1, True],
        [[1], 1, False],
        [[0, 1, 0], 1, False],
        [[0, 0, 1], 1, True],
        [[0, 0, 1], 2, False],
        [[1, 0, 0, 0, 1], 1, True],
        [[1, 0, 0, 0, 1], 2, False],
    ],
)
def test_solution(
    solution: Solution,
    flowerbed: list[int],
    n: int,
    expected_result: bool,
):
    assert solution.canPlaceFlowers(flowerbed, n) == expected_result
