class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        _, prev = intervals[0]
        acum = 0
        for i in range(len(intervals)-1):
            i2 , f2 = intervals[i+1]

            prev = min(prev, f2)

            if i2 < prev:
                acum += 1
            else:
                prev = f2

        return acum