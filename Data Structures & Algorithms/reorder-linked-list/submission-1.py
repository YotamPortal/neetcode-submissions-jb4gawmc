# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondList = slow.next
        slow.next = None

        # 2. Split and Reverse the second half
        curr = secondList
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # 3. Merge the two halves
        firstList = head
        secondList = prev

        while secondList:
            tmp1, tmp2 = firstList.next, secondList.next
            firstList.next = secondList
            secondList.next = tmp1
            firstList, secondList = tmp1, tmp2
