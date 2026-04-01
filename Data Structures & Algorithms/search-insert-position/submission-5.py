class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        v = set()

        while l <= r:
            
            k = (r + l) // 2
            # print(k)
            # if k in v:
            #     print("INN")
            #     if target > nums[k]: 
            #         return k + 1
            #     else:
            #         return k

            if nums[k] == target:
                return k
            elif nums[k] < target:
                print("Peque")
                v.add(k)
                l = k + 1
            else:
                print("GRAND")
                r = k - 1
                v.add(k)
        
        if nums[k] < target:
            print("ELL1")
            return k + 1
        else:
            print("ELL 2")
            return k