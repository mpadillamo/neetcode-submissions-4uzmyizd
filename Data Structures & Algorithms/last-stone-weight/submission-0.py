class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #O(nlogn)
        stones.sort(reverse=True)

        while len(stones) != 1 and len(stones) != 0:
            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
            else:
                stones[0] -= stones[1]
                stones.pop(1)
                stones.sort(reverse=True)
        
        if len(stones) == 1:
            return stones[0]
        else:
            return 0


