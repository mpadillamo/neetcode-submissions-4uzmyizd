class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSup, maxAnt = nums[len(nums)-1], nums[len(nums)-1]

        for i in range(len(nums)-2,-1,-1):
            maxAnt = max(nums[i],maxAnt + nums[i])
            maxSup = max(maxAnt,maxSup)

        return maxSup
        