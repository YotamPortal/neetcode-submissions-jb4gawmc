# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def kth(root):
            if not root: return -1

            var = self.kthSmallest(root.left, self.k)
            if var != -1:
                return var
            if self.k == 1:
                return root.val
            self.k -= 1
            return self.kthSmallest(root.right, self.k)
        self.k = k
        return kth(root)    