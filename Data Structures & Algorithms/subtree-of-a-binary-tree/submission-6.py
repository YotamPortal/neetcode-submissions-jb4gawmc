# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])
        subNode = []
        while q and subRoot:
            node = q.popleft()
            if not node:
                continue
            if node.val == subRoot.val:
                subNode.append(node)
            
            q.append(node.left)
            q.append(node.right)

        res = False
        for node in subNode:
            p = deque([node])
            q = deque([subRoot])
            res = True
            while p and q:
                np, nq = p.popleft(), q.popleft()
                
                if not np and not nq:
                    continue
                if not np or not nq or np.val != nq.val:
                    res = False
                    break

                p.append(np.left)
                p.append(np.right)
                q.append(nq.left)
                q.append(nq.right)
            if res:
                return True

        return res
                                