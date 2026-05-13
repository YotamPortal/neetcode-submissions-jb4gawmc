# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.mapInorderByIdx = {}
        for i in range(len(inorder)):
            self.mapInorderByIdx[inorder[i]] = i

        return self.buildBT(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def buildBT(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd or inStart > inEnd:
            return None
        
        # first preorder element is the current sub-tree root
        root = TreeNode(preorder[preStart])

        inRootIdx = self.mapInorderByIdx[root.val]

        leftTreeSize = inRootIdx - inStart

        root.left = self.buildBT(preorder, preStart + 1, preEnd, inorder, inStart, inRootIdx - 1)
        root.right = self.buildBT(preorder, preStart + leftTreeSize + 1, preEnd, inorder, inRootIdx + 1, inEnd)

        return root