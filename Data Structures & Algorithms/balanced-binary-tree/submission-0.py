# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        bal = True
        def dfs(r):
            nonlocal bal
            if not r:
                return 0
            #Go to left + right
            lh = dfs(r.left)
            lr = dfs(r.right)

            if abs(lh - lr) > 1:
                bal = False
            
            return 1 + max(lh,lr)

        dfs(root)

        return bal
