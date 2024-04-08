"""160. Intersection of Two Linked Lists.

Given the heads of two singly linked-lists headA and headB, return the node at
which the two lists intersect. If the two linked lists have no intersection at
all, return null.

Note that the linked lists must retain their original structure after the
function returns.

--- Custom Judge.

The inputs to the judge are given as follows:

intersectVal - The value of the node where the intersection occurs. This is 0
    if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA to get to the intersected
    node.
skipB - The number of nodes to skip ahead in listB to get to the intersected
    node.
The judge will then create the linked structure based on these inputs and pass
the two heads, headA and headB to your program. If you correctly return the
intersected node, then your solution will be accepted.

Constraints:
    The number of nodes of listA is in the m.
    The number of nodes of listB is in the n.
    1 <= m, n <= 3 * 104
    1 <= Node.val <= 105
    0 <= skipA < m
    0 <= skipB < n
    intersectVal is 0 if listA and listB do not intersect.
    intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{'HEAD ' if self.next is None else ''}[{self.val}]"


class Solution:
    def getIntersectionNode(
        self,
        headA: ListNode,
        headB: ListNode,
    ) -> Optional[ListNode]:
        pointerA = headA
        pointerB = headB

        while pointerA and pointerB:
            if pointerA == pointerB:
                return pointerA

            if pointerA.next is None and pointerB.next is None:
                break

            pointerA = pointerA.next or headB
            pointerB = pointerB.next or headA

        return None


class OldSolution:
    def getIntersectionNode(
        self,
        headA: ListNode,
        headB: ListNode,
    ) -> Optional[ListNode]:
        pointerA, pointerB = headA, headB
        lengthA, lengthB = 1, 1

        while pointerA.next:
            lengthA += 1
            pointerA = pointerA.next

        while pointerB.next:
            lengthB += 1
            pointerB = pointerB.next

        # Return to head
        pointerA, pointerB = headA, headB

        difference = abs(lengthA - lengthB)

        while difference:
            if lengthA > lengthB:
                pointerA = pointerA.next
            elif lengthB > lengthA:
                pointerB = pointerB.next

            difference -= 1

        while pointerA:
            if pointerA == pointerB:
                return pointerA

            pointerA = pointerA.next
            pointerB = pointerB.next

        return None


if __name__ == "__main__":
    last_node = ListNode(1)
    multiple_nodes = ListNode(2, next=last_node)

    nodeA1 = ListNode(3, next=multiple_nodes)
    nodeA = ListNode(4, next=nodeA1)

    nodeB = ListNode(5, next=multiple_nodes)

    solution = Solution()

    print("RESULT:", solution.getIntersectionNode(nodeA, nodeB))
