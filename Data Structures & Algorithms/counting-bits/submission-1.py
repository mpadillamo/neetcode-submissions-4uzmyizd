class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        if n == 2:
            return [0,1,1]
        if n == 3:
            return [0,1,1,2]
        
        arr = [0,1,1,2]

        k = 0
        while 2**k < n:
            k += 1
        
        for i in range(2,k+1):
            for j in range(2**i):
                arr.append(arr[j]+1)
        
        return arr[:n+1]
