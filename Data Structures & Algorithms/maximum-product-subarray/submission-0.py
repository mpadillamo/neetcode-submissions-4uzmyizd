class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        vals = []
        c = 0
        for l in range(len(nums)):
            for r in range(l, len(nums)):
                if r == l:
                    vals.append(nums[r])
                else:
                    vals.append(vals[c-1]*nums[r])
                c += 1
        return max(vals)