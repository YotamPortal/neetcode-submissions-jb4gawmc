# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        q = deque([(root, root.val)])
        count = 0
        while q:
            node, maxVal = q.popleft()
            count += (node.val >= maxVal)
            maxVal = max(node.val, maxVal)
            if node.left: q.append((node.left, maxVal))
            if node.right: q.append((node.right, maxVal))
        return count