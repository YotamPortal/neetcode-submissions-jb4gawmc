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

        tmp1 = l1
        tmp2 = l2
        last1 = None
        last2 = None
        while tmp1 and tmp2:
            n = tmp1.val + tmp2.val + carry
            val, carry = self.carry(n)
            tmp1.val = tmp2.val = val
            last1 = tmp1
            last2 = tmp2
            tmp1 = tmp1.next
            tmp2 = tmp2.next

        left, last, is1 = (tmp1, last1, True) if tmp1 else (tmp2, last2, False) if tmp2 else (None, last2, False)
        while left:
            n = left.val + carry
            left.val, carry = self.carry(n)
            last = left
            left = left.next

        if carry:
            last.next = ListNode(1)

        return l1 if is1 else l2
        
            