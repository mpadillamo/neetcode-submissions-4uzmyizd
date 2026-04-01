class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        v = set()

        while l <= r:
            
            k = (r + l) // 2
            if nums[k] == target:
                return k
            elif nums[k] < target:
                l = k + 1
            else:
                r = k - 1
        
        if nums[k] < target:
            return k + 1
        else:
            return k