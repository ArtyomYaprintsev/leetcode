import pytest

from solution import Solution, ListNode


@pytest.fixture()
def solution():
    return Solution()


@pytest.fixture(name='multiple_nodes')
def create_multiple_nodes():
    node1 = ListNode(val=1, next=None)
    node2 = ListNode(val=2, next=node1)
    node3 = ListNode(val=3, next=node2)
    return node3


def test_with_none_list(solution: Solution):
    assert solution.hasCycle(None) is False


def test_with_only_one_node(solution: Solution):
    node = ListNode(val=1, next=None)
    assert solution.hasCycle(node) is False


def test_with_multiple_nodes(solution: Solution, multiple_nodes: ListNode):
    assert solution.hasCycle(multiple_nodes) is False


def test_with_two_nodes_with_cycle(solution: Solution):
    node1 = ListNode(val=1, next=None)
    node2 = ListNode(val=2, next=node1)
    node1.next = node2
    assert solution.hasCycle(node2) is True


def test_with_multiple_nodes_with_cycle(
    solution: Solution,
    multiple_nodes: ListNode,
):
    head = multiple_nodes.next.next
    head.next = multiple_nodes.next
    assert solution.hasCycle(head) is True
