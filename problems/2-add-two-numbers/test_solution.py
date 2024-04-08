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
    ["list1", "list2", "expected_numbers"],
    [
        pytest.param(
            generate_node([1]),
            generate_node([1]),
            [2],
            id="sum_1_1_equal_2",
        ),
        pytest.param(
            generate_node([1, 0]),
            generate_node([2, 1]),
            [1, 3],
            id="sum_10_21_equal_31",
        ),
        pytest.param(
            generate_node([1, 9]),
            generate_node([2, 9]),
            [8, 4],
            id="sum_19_29_equal_48",
        ),
        pytest.param(
            generate_node([1, 2, 3]),
            generate_node([5, 6, 7, 8]),
            [1, 0, 8, 5],
            id="sum_123_5678_equal_5801",
        ),
        pytest.param(
            generate_node([9, 9, 9, 9, 9, 9, 9]),
            generate_node([9, 9, 9, 9]),
            [8, 9, 9, 9, 0, 0, 0, 1],
            id="sum_9999_9999999_equal_10009998",
        ),
    ],
)
def test_add_two_numbers(
    solution: Solution,
    list1: ListNode,
    list2: ListNode,
    expected_numbers: Sequence[int],
):
    result = solution.addTwoNumbers(list1, list2)

    # node = result

    # while node:
    #     print("VAL", node.val, node.next)
    #     node = node.next

    node = result

    for number in expected_numbers:
        assert node.val == number
        node = node.next
