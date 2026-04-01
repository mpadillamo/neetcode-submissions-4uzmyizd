# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       

        def dfs(root,l,u):
            if not root:
                return True
            else:
                if root.val < u and root.val > l:
                    return dfs(root.right, root.val, u) and dfs(root.left, l, root.val)
                else:
                    return False

        return dfs(root, -9999, 9999)
        
