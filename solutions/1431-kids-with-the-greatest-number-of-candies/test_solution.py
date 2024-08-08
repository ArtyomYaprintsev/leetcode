import pytest

from solution import Solution


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.mark.parametrize(
    [
        'candies',
        'extra',
        'expected',
    ],
    [
        pytest.param(
            [],
            0,
            [],
            id='empty_candies',
        ),
        pytest.param(
            [1],
            0,
            [True],
            id='one_item_candies',
        ),
        pytest.param(
            [1, 1, 1],
            0,
            [True, True, True],
            id='multiple_equal_candies',
        ),
        pytest.param(
            [1, 2, 5, 2, 1],
            3,
            [False, True, True, True, False],
            id='5_max_and_3_extra_candies',
        ),
        pytest.param(
            [4, 1, 2, 1],
            1,
            [True, False, False, False],
            id='4_max_and_1_extra_candies',
        ),
    ],
)
def test_kids_with_candies(
    solution: Solution,
    candies: list[int],
    extra: int,
    expected: list[bool],
):
    assert solution.kidsWithCandies(candies, extra) == expected
