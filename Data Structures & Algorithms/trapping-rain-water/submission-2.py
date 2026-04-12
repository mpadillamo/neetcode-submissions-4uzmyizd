class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 0 # Introduce 2 pointers
        res = 0
        
        # Calculate prefix - O(n)
        prefix = [0]
        m = 0
        for i in range(1,len(height)):
            m = max(m, height[i-1])
            prefix.append(m)

        # Calculate sufix - O(n)
        m = 0
        suffix = [0]
        for i in range(len(height)-2,-1,-1):
            print(i)
            m = max(m,height[i+1])
            suffix.append(m)
        suffix.reverse()

        #Caulculate acum of water - O(n)
        print(prefix)
        print(suffix)
        for i in range(1,len(suffix)-1):
            if height[i] < prefix[i] and height[i] < suffix[i]:
                res += min(prefix[i], suffix[i]) - height[i]
        return res