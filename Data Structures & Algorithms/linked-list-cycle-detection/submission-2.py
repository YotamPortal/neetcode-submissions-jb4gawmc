# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast:
            if slow.next:
                slow = slow.next
            else:
                return False
            if fast.next:
                if fast.next.next:
                    fast = fast.next.next
                else:
                    return False
            else: 
                return False
            if id(slow) == id(fast):
                return True
    
        return False