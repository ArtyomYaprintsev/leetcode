import pytest

from solution import Solution


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.mark.parametrize(
    ['str1', 'str2', 'expected'],
    [
        pytest.param(
            '',
            '',
            '',
            id='empty_for_empty_strings',
        ),
        pytest.param(
            'abc',
            '',
            '',
            id='empty_for_one_empty_string',
        ),
        pytest.param(
            'abc',
            'abc',
            'abc',
            id='two_equal_strings',
        ),
        pytest.param(
            'abcabc',
            'abc',
            'abc',
            id='simple_substring_repeat',
        ),
        pytest.param(
            'abcabcabc',
            'abcabc',
            'abc',
            id='complex_substring_repeat',
        ),
    ]
)
def test_gcd_of_strings(
    solution: Solution,
    str1: str,
    str2: str,
    expected: str,
):
    assert solution.gcdOfStrings(str1, str2) == expected
