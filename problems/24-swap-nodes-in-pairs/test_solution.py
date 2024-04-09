from typing import Sequence
import pytest

from solution import Solution, ListNode


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


def generate_node(nodes: Sequence[int]) -> ListNode:
    """Generates linked list with the following values.

    The first number will be the deepest node and the last one will be the
    head.
    """
    head = None

    for val in nodes:
        head = ListNode(val, head)

    return head


def test_empty_linked_list(solution: Solution):
    assert solution.swapPairs(None) is None


@pytest.mark.parametrize(
    ["linked_list", "expected_values"],
    [
        pytest.param(
            generate_node([1]),
            [1],
            id="swap_with_one_node",
        ),
        pytest.param(
            generate_node([1, 2]),
            [1, 2],
            id="swap_with_two_nodes",
        ),
        pytest.param(
            generate_node([1, 2, 3]),
            [2, 3, 1],
            id="swap_with_three_nodes",
        ),
        pytest.param(
            generate_node([1, 2, 3, 4]),
            [3, 4, 1, 2],
            id="swap_with_four_nodes",
        ),
        pytest.param(
            generate_node([1, 2, 3, 4, 5]),
            [4, 5, 2, 3, 1],
            id="swap_with_five_nodes",
        ),
    ],
)
def test_swap_pairs(
    solution: Solution,
    linked_list: ListNode,
    expected_values: Sequence[int],
):
    result = solution.swapPairs(linked_list)

    node = result

    for value in expected_values:
        assert node.val == value
        node = node.next
