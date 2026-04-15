class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # Starting at 0
        islands = {}

        # Set for marking visited
        visited = set()

        
        def dfs(i, j, key):
            
            #Append visited
            visited.add((i,j))
            print((i,j))
            if grid[i][j] == 1:

                #Append 1 to the islands
                islands[k] += 1

                # Go to other positions
                if i + 1 < len(grid) and (i+1,j) not in visited:
                    dfs(i+1,j,k)

                if i-1 >= 0  and (i-1, j) not in visited:
                    dfs(i-1,j,k)
                
                if j + 1 < len(grid[0]) and (i,j+1) not in visited:
                    dfs(i,j+1,k)
                
                if j - 1 >= 0 and (i,j-1) not in visited:
                    dfs(i,j-1,k)
            
            return


        # Pass thorugh every position
        k = 0
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if (a,b) not in visited:
                    k += 1
                    islands[k] = 0

                    dfs(a,b,k)

        return max(islands.values())
