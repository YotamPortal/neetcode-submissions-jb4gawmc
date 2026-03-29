# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        count, curr = 0, head
        while curr:
            count += 1
            curr = curr.next

        if count < n:
            return None

        removeId = count - n + 1
        i = 0
        prev, curr = None, head
        while curr:
            i += 1
            if i == removeId:
                if prev:
                    prev.next = curr.next
                    return head
                elif curr.next:
                    return curr.next
                else:
                    return None
            prev = curr
            curr = curr.next
        return head
        