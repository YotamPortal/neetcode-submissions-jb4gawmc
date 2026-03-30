# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_val, q_val = p.val, q.val
        it = root
        while True:
            if it.val > max(p_val, q_val):
                it = it.left
            elif it.val < min(p_val, q_val):
                it = it.right
            else:
                return it
        return it
            