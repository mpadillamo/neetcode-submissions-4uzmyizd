class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ref = []
        for e in s1:
            ref.append(e)
        ref.sort()
        l, r = 0, len(s1)

        while r <= len(s2):
            c = []
            for i in s2[l:r]:
                c.append(i)
            c.sort()
            print(c)
            if c == ref:
                return True
            l += 1
            r += 1
        return False