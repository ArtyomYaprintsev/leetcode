"""2. Add Two Numbers.

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have
        leading zeros.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        head = ListNode()
        cur = head

        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry

            carry = val // 10
            val %= 10

            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next

    def addTwoNumbersPreOptimized_2(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        # find the greater by nodes count linked list
        pointer1 = l1
        pointer2 = l2

        while pointer1 and pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        # if only one of the pointers is None, then greater by nodes count
        # linked list with not None pointer
        greater = l1 if pointer2 is None else l2
        lower = l2 if greater == l1 else l1

        # sum each node of the lists
        while greater.next:
            # lower can be None earlier then greater, so add `getattr` usage to
            # avoid `AttributeError`
            greater.val += getattr(lower, "val", 0)

            # move second digits to the next place number
            greater.next.val += greater.val // 10
            greater.val %= 10

            greater = greater.next
            lower = getattr(lower, "next", None)

        # the last digits iteration has been missing
        greater.val += getattr(lower, "val", 0)

        # if the last sum create new place number, so create new tail node and
        # link it with previous last node of the greater linked list
        if greater.val >= 10:
            greater.next = ListNode(val=greater.val // 10, next=None)
            greater.val %= 10

        # return greater linked list
        return l1 if pointer2 is None else l2

    def addTwoNumbersPreOptimized(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        # find the greater by nodes count linked list
        pointer1 = l1
        pointer2 = l2

        while pointer1 and pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        # if only one of the pointers is None, then greater by nodes count
        # linked list with not None pointer
        greater = l1 if pointer2 is None else l2
        lower = l2 if greater == l1 else l1

        next_place_number = 0
        previous_greater = greater

        # sum each node of the lists
        while greater:
            # lower can be None earlier then greater, so add `getattr` usage to
            # avoid `AttributeError`
            current_greater_and_lower_digit_sum = (
                greater.val
                + getattr(lower, "val", 0)
                + next_place_number
            )

            # split digits sum
            next_place_number = current_greater_and_lower_digit_sum // 10
            current_greater_and_lower_digit_sum %= 10

            greater.val = current_greater_and_lower_digit_sum

            previous_greater = greater
            greater = greater.next
            lower = getattr(lower, "next", None)

        # if the last sum create new place number, so create new tail node and
        # link it with previous last node of the greater linked list
        if next_place_number:
            previous_greater.next = ListNode(val=next_place_number, next=None)

        # return greater linked list
        return l1 if pointer2 is None else l2
