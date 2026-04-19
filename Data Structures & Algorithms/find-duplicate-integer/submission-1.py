class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        f, s1, s2 = 0, 0, 0

        # Intersection
        s1 = nums[s1]
        f = nums[nums[f]]

        while s1 != f:
            s1 = nums[s1]
            f = nums[nums[f]]

        while s1 != s2:
            s1 = nums[s1]
            s2 = nums[s2]
        
        return s1
