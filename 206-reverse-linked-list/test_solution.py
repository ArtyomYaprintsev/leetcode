import pytest

from solution import Solution, ListNode


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


def test_with_none_node(solution: Solution):
    assert solution.reverseList(None) is None


def test_with_one_node(solution: Solution):
    node = ListNode(1)

    reversed_node = solution.reverseList(node)

    assert reversed_node.val == node.val
    assert reversed_node.next is None


def test_with_two_node(solution: Solution):
    node1 = ListNode(1)
    node2 = ListNode(2, next=node1)

    reversed_node = solution.reverseList(node2)

    assert reversed_node.val == node1.val
    assert reversed_node.next.val == node2.val
    assert reversed_node.next.next is None


def test_with_multiple_nodes(solution: Solution):
    node1 = ListNode(1)
    node2 = ListNode(2, next=node1)
    node3 = ListNode(3, next=node2)

    reversed_node = solution.reverseList(node3)

    assert reversed_node.val == node1.val
    assert reversed_node.next.val == node2.val
    assert reversed_node.next.next.val == node3.val
    assert reversed_node.next.next.next is None
