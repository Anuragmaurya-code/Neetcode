class Solution:
    def exist(self, board, word: str) -> bool:
        ROWS,COLS=len(board),len(board[0])
        def backtrack(i,r,c,track):
            if i==len(word):
                return True
            if r>=ROWS or c>=COLS or r<0 or c<0 or board[r][c]!=word[i] or (r,c) in track:
                return False
            track.append((r,c))
            if backtrack(i+1,r-1,c,track) or backtrack(i+1,r,c-1,track) or backtrack(i+1,r+1,c,track) or backtrack(i+1,r,c+1,track):
                return True
            return False
        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(0,i,j,[]):
                    return True
        return False



        

        
x=Solution()
print(x.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))