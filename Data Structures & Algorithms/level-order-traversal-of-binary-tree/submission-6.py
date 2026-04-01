# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final_list = defaultdict(list)
        lvl = 0

        def dfs(root, lvl):
            nonlocal final_list
            if root:
                final_list[lvl].append(root.val)
                dfs(root.left, lvl+1)
                dfs(root.right, lvl+1)


            else:
                return
        dfs(root,lvl)

        res = []

        for k, val in  final_list.items():
            res.append(val)

        print(res)
        return res
        