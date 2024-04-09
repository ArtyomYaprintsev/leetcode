"""24. Swap Nodes in Pairs.

Given a linked list, swap every two adjacent nodes and return its head. You
must solve the problem without modifying the values in the list's nodes (i.e.,
only nodes themselves may be changed.)

Constraints:
    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            current.next = second
            first.next = second.next
            second.next = first

            current = first

        return dummy.next

    def swapPairsNotOptimized(
        self,
        head: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        current = head

        prev = dummy

        while current and current.next:
            prev.next = current.next
            prev = current

            temp_next_next = current.next.next

            current.next.next = current
            current.next = temp_next_next

            current = current.next

        return dummy.next
