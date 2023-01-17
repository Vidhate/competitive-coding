# https://leetcode.com/problems/valid-sudoku/submissions/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        grid = []
        for i in range(9):
            rowmap = [int(c) for c in board[i] if not c=='.']
            if len(set(rowmap))<len(rowmap):
                return False
            col = [x[i] for x in board]
            colmap = [int(r) for r in col if not r=='.']
            if len(set(colmap))<len(colmap):
                return False
            
            j = (i%3)*3
            k = (i//3)*3
            grid = []
            
            for jc in range(j,j+3):
                for kc in range(k, k+3):
                    val = board[kc][jc]
                    if not val=='.':
                        grid.append(int(val))
                        
            if len(set(grid))<len(grid):
                return False
            
        return True