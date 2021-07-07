# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        output = str(self.val)
        next = self.next
        while next:
            output += f', {next.val}'
            next = next.next
        return output


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass


if __name__ == '__main__':
    sol = Solution()
    tests = [
        (
            ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3))),
            ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4))),
        ),
    ]
    for l1, l2 in tests:
        print(f'{l1} + {l2} = {sol.addTwoNumbers(l1, l2)}')
