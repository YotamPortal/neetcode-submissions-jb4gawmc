# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        left = dummy
        right = head

        # move right n times
        for _ in range(n):
            right = right.next

        # move right and left until right reach the end
        while right:
            right = right.next
            left = left.next

        # left now is one node before the one to delete
        left.next = left.next.next

        return dummy.next