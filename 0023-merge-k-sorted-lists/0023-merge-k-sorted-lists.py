import heapq


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        heap = []
        counter = 0

        # Put the first node of each linked list into the heap
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1

        dummy = ListNode(0)
        current = dummy

        while heap:
            _, _, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            # Add the next node from the same list
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next