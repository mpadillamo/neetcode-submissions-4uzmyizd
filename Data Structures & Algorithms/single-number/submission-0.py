class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ac = 0

        for i in nums:
            ac = ac ^ i
        
        return ac