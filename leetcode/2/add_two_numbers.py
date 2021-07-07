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
        # iterate through l1 and l2 to retrieve the numbers
        num1 = [l1.val]
        next = l1.next
        while next:
            num1.append(next.val)
            next = next.next
        num2 = [l2.val]
        next = l2.next
        while next:
            num2.append(next.val)
            next = next.next

        # do first iteration
        val = num1[-1] + num2[-1]
        carry = True if val // 10 != 0 else False
        val = val % 10
        parent_node = ListNode(val=val)

        prev = parent_node 
        num_iterations = max(len(num1), len(num2))
        for i in range(num_iterations - 2, -1, -1):
            # do the math
            val = num1[i] + num2[i]
            val += 1 if carry else 0 
            carry = True if val // 10 != 0 else False
            val = val % 10
            
            # create and add new node to end of list
            node = ListNode(val=val, next=None)
            prev.next = node
            prev = node
        return parent_node

        

if __name__ == '__main__':
    sol = Solution()
    tests = [
        (
            ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3))),
            ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4))),
        ),
        (
            ListNode(val=0),
            ListNode(val=0),
        ),
    ]
    for l1, l2 in tests:
        print(f'{l1} + {l2} = {sol.addTwoNumbers(l1, l2)}')
