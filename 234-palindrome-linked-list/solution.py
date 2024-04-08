"""234. Palindrome Linked List.

Given the head of a singly linked list, return true if it is a palindrome or
false otherwise.

Constraints:
    The number of nodes in the list is in the range [1, 10^5].
    0 <= Node.val <= 9
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # T 265ms M 27.4mb
        slow, fast = head, head

        prev = None

        # reach the middle with `slow` pointer and reverse the first part of
        # the linked list
        while fast and fast.next:
            temp_slow = slow.next

            fast = fast.next.next

            slow.next = prev
            prev = slow
            slow = temp_slow

        left = prev
        right = slow if fast is None else slow.next

        # check palindrome
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

    def isPalindrome_2(self, head: Optional[ListNode]) -> bool:
        # T 292ms M 32.1mb
        if head.next is None:
            return True

        slow, fast = head, head

        # reach the middle with `slow` pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second part of the linked list
        prev = None

        while slow:
            next = slow.next

            slow.next = prev
            prev = slow
            slow = next

        # check palindrome
        left = head
        right = prev

        while left and right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
