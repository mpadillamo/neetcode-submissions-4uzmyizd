class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            
            # Append solution
            if total == target:
                res.append(curr.copy())
                return
            
            # Discard solution
            if i >= len(nums) or total > target:
                return
            
            # First option include a candidate
            curr.append(nums[i])
            dfs(i,curr, total + nums[i])
            
            # Second option skip the candidate
            curr.pop()
            dfs(i+1, curr, total)
        

        dfs(0,[],0)

        return res


        