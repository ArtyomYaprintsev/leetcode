"""206. Reverse Linked List.

Given the head of a singly linked list, reverse the list, and return the
reversed list.

Constraints:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        new_head = head

        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head

        head.next = None
        return new_head

    def reverseListWithOptimizedIteration(
        self,
        head: Optional[ListNode],
    ) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            temp_current_next = current.next

            current.next = prev
            prev = current
            current = temp_current_next

        return prev

    def reverseListWithRecursion_2(
        self,
        head: Optional[ListNode],
    ) -> Optional[ListNode]:
        # 32ms 17.7 mb
        if head is None:
            return None

        if head.next is None:
            return head

        next = head.next
        head.next = None

        if next.next is None:
            next.next = head
            return next

        new_head = self.reverseListWithRecursion_2(next)

        next.next = head

        return new_head

    def reverseListWithRecursion_1(
        self,
        head: Optional[ListNode],
        prev: Optional[ListNode] = None,
    ) -> Optional[ListNode]:
        if head is None:
            return prev

        next = head.next
        head.next = prev

        return self.reverseListWithRecursion_1(next, head)

    def reverseListWithRecursion(
        self,
        head: Optional[ListNode],
        prev: Optional[ListNode] = None,
    ) -> Optional[ListNode]:
        if head is None:
            return prev

        return self.reverseListWithRecursion(
            head.next,
            ListNode(val=head.val, next=prev),
        )

    def reverseListWithIteration(
        self,
        head: Optional[ListNode],
    ) -> Optional[ListNode]:
        if head is None:
            return None

        pointer = head
        new_head: Optional[ListNode] = None

        while pointer:
            new_head = ListNode(val=pointer.val, next=new_head)
            pointer = pointer.next

        return new_head
