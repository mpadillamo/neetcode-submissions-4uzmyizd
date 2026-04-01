class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        vals = []

        def dfs(i, j, m , n):
            if i == m and j == n:
                vals.append(1)
                return
            elif i < m and j < n:
                dfs(i+1,j,m,n)
                dfs(i,j+1,m,n)

            elif i < m:
                dfs(i+1,j,m,n)

            elif j < n:
                dfs(i,j+1,m,n)

        dfs(1,1,m,n)

        return len(vals)