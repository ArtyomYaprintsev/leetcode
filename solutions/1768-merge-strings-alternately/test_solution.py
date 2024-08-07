import pytest

from solution import Solution


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.mark.parametrize(
    ['word1', 'word2', 'expected'],
    [
        pytest.param(
            '',
            '',
            '',
            id='merge_empty_strings',
        ),
        pytest.param(
            'abc',
            '',
            'abc',
            id='merge_string_with_empty',
        ),
        pytest.param(
            'abc',
            '123',
            'a1b2c3',
            id='merge_strings',
        ),
        pytest.param(
            'abcde',
            '123',
            'a1b2c3de',
            id='merge_strings_with_different_lengths_1',
        ),
        pytest.param(
            'abc',
            '12345',
            'a1b2c345',
            id='merge_strings_with_different_lengths_2',
        ),
    ]
)
def test_merge_strings_alternately(
    solution: Solution,
    word1: str,
    word2: str,
    expected: str,
):
    assert solution.mergeAlternately(word1, word2) == expected
