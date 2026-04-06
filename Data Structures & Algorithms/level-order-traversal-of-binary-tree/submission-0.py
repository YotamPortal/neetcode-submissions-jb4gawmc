# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traversal(self, root, level):
        if not root:
            return None
        if len(self.res) == level:
            self.res.append([])
        self.res[level].append(root.val)
        self.traversal(root.left, level + 1)
        self.traversal(root.right, level + 1) 
        

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        self.traversal(root, 0)
        return self.res

