import pytest

from solution import Solution


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.mark.parametrize(
    ["input_s", "input_k", "output"],
    [
        ("a", 1, 1),
        ("b", 1, 0),
        ("abciiidef", 3, 3),
        ("aeiou", 2, 2),
        ("leetcode", 3, 2),
    ],
)
def test_solution(solution: Solution, input_s: str, input_k: int, output: int):
    assert solution.maxVowels(input_s, input_k) == output
