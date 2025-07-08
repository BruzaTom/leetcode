# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0

        # add or carry in the edge case of un even integers
        while l1 or l2 or carry:
            #place value in variable if there is a value still else value is zero
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            # extracts the digit that needs to be carried over to the next step.
            carry = total // 10

            # makes the value of next only the ones place from total 
            current.next = ListNode(total % 10)  
            
            #update pointers
            current = current.next
            if l1: l1 = l1.next if l1 else None
            if l2: l2 = l2.next if l2 else None

        return dummy.next

