"""21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        if (list2 is None) or (list1 is not None and list2.val > list1.val):
            return ListNode(
                val=list1.val,
                next=self.mergeTwoLists(list1.next, list2),
            )

        return ListNode(
            val=list2.val,
            next=self.mergeTwoLists(list1, list2.next),
        )
