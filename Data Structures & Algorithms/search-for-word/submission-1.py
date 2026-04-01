class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        wordCells = set()
        comp = set()
        
        def dfs(r, c, wordCells, letter):
            if ((r,c) in wordCells
                or r < 0
                or c < 0
                or r >= m
                or c >= n
                or 0 in comp):
                return
            if board[r][c] == word[letter]:
                wordCells.add((r,c))
                if letter == len(word)-1:
                    comp.add(0)
                    return
                dfs(r-1,c,wordCells.copy(),letter+1)
                dfs(r+1,c,wordCells.copy(),letter+1)
                dfs(r,c+1,wordCells.copy(),letter+1)
                dfs(r,c-1,wordCells.copy(),letter+1)
            else:
                return
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    dfs(i,j,wordCells.copy(),0)
                if 0 in comp:
                    break
            if 0 in comp:
                break
        if 0 in comp:
            return True
        else:
            return False

        
