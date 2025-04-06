import pytest

from solution import Solution


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.mark.parametrize(
    ["init_str", "expected_str"],
    [
        ["a", "a"],
        ["IceCreAm", "AceCreIm"],
        ["abcde", "ebcda"],
        ["AbcDe", "ebcDA"],
    ],
)
def test_solution(solution: Solution, init_str: str, expected_str: str):
    assert solution.reverseVowels(init_str) == expected_str
