class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        max_val = {}

        for e in nums:
            max_val[e] = max_val.get(e, 0) + 1
        
        m = 0
        res = 0
        for k, v in max_val.items():
            if v > m:
                res = k
                m = v
        
        return res
