# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        tail = None
        prev = None
        if list1.val < list2.val:
            tail = self.mergeTwoLists(list1.next, list2)
            list1.next = tail
            prev = list1
        else:
            tail = self.mergeTwoLists(list1, list2.next)
            list2.next = tail
            prev = list2
        
        return prev        