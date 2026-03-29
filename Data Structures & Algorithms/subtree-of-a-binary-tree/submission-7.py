# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(a, b):
            p = deque([a])
            q = deque([b])
            while p and q:
                np, nq = p.popleft(), q.popleft()
                
                if not np and not nq:
                    continue
                if not np or not nq or np.val != nq.val:
                    return False

                p.append(np.left)
                p.append(np.right)
                q.append(nq.left)
                q.append(nq.right)

            return True

        q = deque([root])
        while q and subRoot:
            node = q.popleft()
            if not node:
                continue
            if node.val == subRoot.val:
                if isSame(node, subRoot):
                    return True
            
            q.append(node.left)
            q.append(node.right)
        
        return False
                                