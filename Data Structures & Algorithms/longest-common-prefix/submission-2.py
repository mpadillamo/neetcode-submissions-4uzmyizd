class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = []
        res = ""
        #N
        for s in strs[0]:
            pre.append(s)
        
        print(pre)
        for p in strs:

            while len(pre) > len(p):
                pre.pop()


            for i in range(len(pre)-1,-1,-1):
                if p[i] != pre[i]:
                    pre = pre[:i]
                if not pre:
                    return res
        
        

        for e in pre:
            res += e
        
        return res