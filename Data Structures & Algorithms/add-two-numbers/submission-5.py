# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def carry(self, n):
        if n < 10:
            return (n, 0)
        return (n % 10, 1)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        head = dummy

        while l1 and l2:
            n = l1.val + l2.val + carry
            val, carry = self.carry(n)
            head.next = ListNode(val)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        
        left = l1 if l1 else l2 if l2 else None
        while left:
            n = left.val + carry
            val, carry = self.carry(n)
            head.next = ListNode(val)
            head = head.next
            left = left.next

        if carry:
            head.next = ListNode(1)

        return dummy.next    

