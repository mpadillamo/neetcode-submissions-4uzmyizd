class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        from collections import Counter
        res = []
        def addBr(ori: str):

            charCount = Counter(ori)
            if charCount[")"] > charCount["("]:
                return

            if len(ori) == 2*n and charCount[")"] == charCount["("]:
                res.append(ori)
                return
            elif len(ori) == 2*n:
                return
            else:
                addBr(ori+")")
                addBr(ori+"(")
        
       
        addBr(")")
        addBr("(")
        return res