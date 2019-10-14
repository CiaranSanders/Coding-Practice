# Ciaran Sanders
# October 13 2019
# Merge K sorted lists

import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
 def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        merged = None
        minHeap = []

        if len(lists) == 0:
            return None

        # Create a min heap out of the K linked lists O(2N)
        for x in lists:
            while x is not None:
                minHeap.append(x.val)
                x = x.next
        if len(minHeap) == 0:
            return None
        heapq.heapify(minHeap)

        # Use the min heap to re-combine the K linked lists into one
        merged = ListNode(heapq.heappop(minHeap))
        it = merged
        for x in range(len(minHeap)):
            it.next = ListNode(heapq.heappop(minHeap))
            it = it.next

        return merged



if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(4)
    list1.next.next = ListNode(5)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next = ListNode(4)
    list3 = ListNode(2)
    list3.next = ListNode(6)
    sortMe = [list1,list2,list3]

    sol = Solution()
    sortedList = sol.mergeKLists(sortMe)

    while sortedList != None:
        print(sortedList.val)
        sortedList = sortedList.next
