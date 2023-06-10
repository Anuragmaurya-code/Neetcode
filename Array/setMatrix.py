class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=set()
        column=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] ==0:
                    row.add(i)
                    column.add(j)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in row or j in column:
                    matrix[i][j] =0

ans=Solution()
ans.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])