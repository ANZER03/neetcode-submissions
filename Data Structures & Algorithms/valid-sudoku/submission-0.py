class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            row = [r for r in row if r != "."]
            if len(set(row)) != len(row) :
                return False
        
        for c in range(9):
            temp_col = []
            for r in range(9):
                if board[r][c] != "." :
                    temp_col.append(board[r][c])
            
            if len(set(temp_col)) != len(temp_col) :
                return False
        

        for i_r in range(0 , 9, 3) :
            for i_c in range(0 , 9, 3) :
                temp_col = []
                for r in range(i_r, i_r + 3):
                    # temp_col = []
                    for c in range(i_c , i_c + 3):
                        if board[r][c] != "." :
                            temp_col.append(board[r][c])
                
                    if len(set(temp_col)) != len(temp_col) :
                        return False
        return True
        