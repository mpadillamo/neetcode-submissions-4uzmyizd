class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        maxTemp = []
        idList = []
        res = {}

        for k, v in enumerate(temperatures):
            res[k] = 0 # Initialitze dict
        maxTemp.append(temperatures[0])
        idList.append(0)
        for i in range(1,len(temperatures)):
            
            
            while maxTemp and idList and temperatures[i]>maxTemp[-1] and i > idList[-1]:
                res[idList[-1]] =  i - idList[-1]
                maxTemp.pop()
                idList.pop()
            maxTemp.append(temperatures[i])
            idList.append(i)
        out = []
        
        for k, v in res.items():
            out.append(v)
        return out
            
        
        
    

        


            