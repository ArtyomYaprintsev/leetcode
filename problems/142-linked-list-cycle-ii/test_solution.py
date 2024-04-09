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


# def test_cycle
