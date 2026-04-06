# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS - for each depth, look from right to left
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res, q = [], deque([root])
        while q:
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                if i == 0:
                    res.append(node.val)
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
        return res
                