class Solution:
    def isValid(self, s: str) -> bool:
        heap = []
        for e in s:
            if e == "(":
                heap.append("(")
            elif e == "{":
                heap.append("{")
            elif e == "[":
                heap.append("[")
            elif e == "]":
                if heap and heap[-1] == "[":
                    heap.pop()
                else:
                    return False
            elif e == "}":
                if heap and heap[-1] == "{":
                    heap.pop()
                else:
                    return False
            elif e == ")":
                if heap and heap[-1] == "(":
                    heap.pop()
                else:
                    return False
        
        if not heap:
            return True
        else:
            return False
