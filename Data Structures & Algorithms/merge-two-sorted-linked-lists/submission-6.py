# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        newHead = None
        newlistPtr = None
        while l1 or l2:
            if l1 and l2:
                if l1.val > l2.val:
                    if newHead:
                        newlistPtr.next = l2
                    else:
                        newHead = l2
                    newlistPtr = l2
                    l2 = l2.next
                else:
                    if newHead:
                        newlistPtr.next = l1
                    else:
                        newHead = l1
                    newlistPtr = l1
                    l1 = l1.next
            else:
                if l1:
                    if newHead:
                        newlistPtr.next = l1
                    else:
                        newHead = l1
                    newlistPtr = l1
                elif l2:
                    if newHead:
                        newlistPtr.next = l2
                    else:
                        newHead = l2
                    newlistPtr = l2
                break
        return newHead   