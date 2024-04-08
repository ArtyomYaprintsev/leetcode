import pytest

from solution import Solution, ListNode


@pytest.fixture(name="solution")
def create_solution():
    return Solution()


@pytest.fixture(name='last_node')
def create_last_node():
    return ListNode(1)


@pytest.fixture(name='multiple_nodes')
def create_multiple_nodes(last_node: ListNode):
    return ListNode(3, next=last_node)


def test_with_different_last_nodes(solution: Solution):
    node1 = ListNode(1)
    node2 = ListNode(1)

    assert solution.getIntersectionNode(node1, node2) is None


def test_with_equal_last_nodes(solution: Solution, last_node: ListNode):
    assert solution.getIntersectionNode(last_node, last_node) == last_node


def test_with_multiple_nodes_without_intersection(
    solution: Solution,
    multiple_nodes: ListNode,
):
    new_last_node = ListNode(1)
    new_multiple_nodes = ListNode(1, next=new_last_node)

    assert solution.getIntersectionNode(
        multiple_nodes,
        new_multiple_nodes,
    ) is None


def test_with_equal_multiple_nodes(
    solution: Solution,
    multiple_nodes,
):
    assert solution.getIntersectionNode(
        multiple_nodes,
        multiple_nodes,
    ) == multiple_nodes


def test_with_different_multiple_nodes_with_intersection(
    solution: Solution,
    multiple_nodes: ListNode,
):
    nodeA1 = ListNode(1, next=multiple_nodes)
    nodeA = ListNode(2, next=nodeA1)

    nodeB = ListNode(2, next=multiple_nodes)

    assert solution.getIntersectionNode(nodeA, nodeB) == multiple_nodes
