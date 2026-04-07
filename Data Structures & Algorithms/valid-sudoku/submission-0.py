class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Generate a hashmap
        # O(3n) space
        res_dict = defaultdict(list)

        # O(n^2) loop
        for r in range(len(board)):
            for c in range(len(board[0])):
                #Insert in row
                if board[r][c] in res_dict["r"+str(r)]:
                    return False
                elif board[r][c] != ".":
                    res_dict["r"+str(r)].append(board[r][c])

                
                #Insert in column
                if board[r][c] in res_dict["c"+str(c)]:
                    return False
                elif board[r][c] != ".":
                    res_dict["c"+str(c)].append(board[r][c])

                #Insert in quadrant
                q1 = r // 3
                q2 = c // 3 + 1

                if board[r][c] in res_dict["q"+str(q1)+str(q2)]:
                    return False
                elif board[r][c] != ".":
                    res_dict["q"+str(q1)+str(q2)].append(board[r][c])
        return True
        