# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.subHead = []
        def subDfs(root, subRoot):
            if not root:
                return None
            if root.val == subRoot.val:
                self.subHead.append(root)
            subDfs(root.left, subRoot)
            subDfs(root.right, subRoot)

        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        subDfs(root, subRoot)

        for node in self.subHead:
            if isSameTree(node, subRoot):
                return True
        
        return False
        


            