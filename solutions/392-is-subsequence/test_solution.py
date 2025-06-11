import pytest

from solution import Solution


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.mark.parametrize(
    ["input_substr", "input_str", "expected"],
    [
        ["", "", True],
        ["a", "a", True],
        ["ab", "ab", True],
        ["ab", "ba", False],
        ["ab", "axb", True],
        ["ab", "ax", False],
        ["ab", "axxx", False],
        ["ab", "xxxaxxx", False],
        ["ab", "eidbaoo", False],
        ["ab", "eadbaoo", True],
        ["abc", "ahbgdc", True],
        ["axc", "ahbgdc", False],
    ],
)
def test_solution(
    solution: Solution,
    input_substr: str,
    input_str: str,
    expected: bool,
):
    assert solution.isSubsequence(input_substr, input_str) == expected
