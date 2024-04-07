import pytest

from solution import ListNode, Solution


@pytest.fixture(name="solution")
def solution():
    return Solution()


def test_solution_with_none(solution: Solution):
    list1 = None
    list2 = None

    assert solution.mergeTwoLists(list1, list2) is None


def test_solution_with_one_node(solution: Solution):
    list1 = ListNode(1)
    list2 = None

    result = solution.mergeTwoLists(list1, list2)

    assert result.val == 1 and result.next is None


def test_solution_with_two_nodes(solution: Solution):
    list1 = ListNode(1)
    list2 = ListNode(2)

    result = solution.mergeTwoLists(list1, list2)

    result_head = result.next

    assert result.val == list1.val
    assert result_head is not None
    assert result_head.val == list2.val
    assert result_head.next is None
