class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if k == 0: #K = 0
            return False
        
        while k > 0:
            a = 0
            while a + k <= len(nums) - 1:
                if nums[a] == nums[a + k]:
                    return True

                a += 1 


            k -= 1 #Quitar
        return False