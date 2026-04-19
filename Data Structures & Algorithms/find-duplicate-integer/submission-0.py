class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for el in nums:
            c = 0
            for n in nums:
                if n == el:
                    c += 1
                    if c == 2:
                        return n
        
        return 0