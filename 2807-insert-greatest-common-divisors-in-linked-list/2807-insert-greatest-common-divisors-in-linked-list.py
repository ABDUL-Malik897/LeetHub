# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head.next

        while fast:
            a = slow.val
            b = fast.val

            # Calculate GCD using Euclid's algorithm
            while b != 0:
                a, b = b, a % b

            new_node = ListNode(a)
            slow.next = new_node
            new_node.next = fast

            # Move to the next original pair
            slow = fast
            fast = fast.next

        return head