from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row=defaultdict(set) # row={
            # 1:{1,2,34,5} this is a set with some values
        #}
        # column={
            # 1:{1,2,34,5} this is a set with some values
        #}
        # square = {(0, 0): {'8', '3', '9', '6'}, (0, 1): {'5', '9', '7', '1'}})
        col=defaultdict(set)
        square=defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] =='.':
                    continue
                
                if (board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[( r// 3,c // 3)]):
                    return False
                
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[( r // 3,c // 3)].add(board[r][c])
       
        return True
                    
        
    
                
        
x=Solution()
board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


print(x.isValidSudoku(board))