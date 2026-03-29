# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = deque([p])
        stack_q = deque([q])
        while stack_p and stack_q:
            node1, node2 = stack_p.popleft(), stack_q.popleft()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False

            stack_p.append(node1.left)
            stack_p.append(node1.right)
            stack_q.append(node2.left)
            stack_q.append(node2.right)

        return True