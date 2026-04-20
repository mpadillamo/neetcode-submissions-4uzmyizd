# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        lvls = set()

        def dfs(root, lvl):
            
            if not root:
                return

            # If not predecesor level
            if lvl not in lvls:
                res.append(root.val)
                lvls.add(lvl)
            
            dfs(root.right, lvl + 1)
            dfs(root.left, lvl + 1)

            return
        
        dfs(root,0)
        return res
        