import pytest

from solution import Solution


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.mark.parametrize(
    ["input_str", "expected_str"],
    [
        ("", ""),
        ("a", "a"),
        ("abc", "abc"),
        ("a b c", "c b a"),
        ("   a", "a"),
        ("a   ", "a"),
        ("   a   ", "a"),
        ("   a   b   c   ", "c b a"),
    ],
)
def test_solution(solution: Solution, input_str: str, expected_str: str):
    assert solution.reverseWords(input_str) == expected_str
