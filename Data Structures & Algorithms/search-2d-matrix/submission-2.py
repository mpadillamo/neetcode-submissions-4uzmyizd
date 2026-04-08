class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Binary search for row --> matrix[x][0]
        l, r = 0, len(matrix) - 1
        k = 0
        while l<=r:
            k = (l+r)//2
            if matrix[k][0] == target:
                return True
            elif matrix[k][0] > target:
                r = k - 1
            else:
                l = k + 1
        
        if matrix[k][0] > target:
            k -= 1
        
        j = 0
        l, r = 0, len(matrix[0]) - 1
        print(k)
        while l<=r:
            j = (l+r)//2
            if matrix[k][j] == target:
                return True
            elif matrix[k][j] > target:
                r = j - 1
            else:
                l = j + 1
        return False

        

        