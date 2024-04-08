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


@pytest.mark.parametrize(
    ["linked_list", "nth_from_end", "expected_values"],
    [
        pytest.param(
            generate_node([1]),
            1,
            [],
            id="remove_the_only_one_node",
        ),
        pytest.param(
            generate_node([1, 2, 3]),
            1,
            [3, 2],
            id="remove_the_last_node",
        ),
        pytest.param(
            generate_node([1, 2, 3]),
            3,
            [2, 1],
            id="remove_the_first_node",
        ),
        pytest.param(
            generate_node([1, 2, 3, 4, 5]),
            2,
            [5, 4, 3, 1],
            id="remove_the_center_node",
        ),
        pytest.param(
            generate_node([1, 2, 3, 4, 5]),
            4,
            [5, 3, 2, 1],
            id="remove_the_center_node",
        ),
    ],
)
def test_add_two_numbers(
    solution: Solution,
    linked_list: ListNode,
    nth_from_end: int,
    expected_values: Sequence[int],
):
    result = solution.removeNthFromEnd(linked_list, nth_from_end)

    node = result

    while node:
        print("VAL", node.val, node.next)
        node = node.next

    node = result

    for number in expected_values:
        assert node.val == number
        node = node.next
