from typing import Sequence
import pytest

from solution import Solution, ListNode


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


def generate_node(nodes: Sequence[int]) -> ListNode:
    head = None

    for val in nodes:
        head = ListNode(val, head)

    return head


def test_is_palindrome_with_one_node(solution: Solution):
    node = generate_node([1])
    assert solution.isPalindrome(node)


@pytest.mark.parametrize(
    "nodes, expected",
    [
        pytest.param(
            (1, 1),
            True,
            id="ll_is_palindrome_with_equal_two_nodes",
        ),
        pytest.param(
            (1, 2),
            False,
            id="ll_is_not_palindrome_with_different_two_nodes",
        ),
        pytest.param(
            (1, 2, 3, 2, 1),
            True,
            id="ll_is_palindrome_with_different_five_nodes",
        ),
        pytest.param(
            (1, 2, 3, 2, 5),
            False,
            id="ll_is_not_palindrome_with_different_five_nodes",
        ),
        pytest.param(
            (1, 2, 3, 3, 2, 1),
            True,
            id="ll_is_palindrome_with_different_six_nodes",
        ),
        pytest.param(
            (1, 2, 3, 4, 2, 1),
            False,
            id="ll_is_not_palindrome_with_different_six_nodes",
        ),
    ],
)
def test_is_palindrome_with_multiple_nodes(
    solution: Solution,
    nodes: ListNode,
    expected: bool,
):
    assert solution.isPalindrome(generate_node(nodes)) == expected
