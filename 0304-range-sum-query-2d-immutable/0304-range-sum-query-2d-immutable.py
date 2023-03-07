class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.prefix[r+1][c+1] = matrix[r][c] - self.prefix[r][c] + self.prefix[r+1][c] + self.prefix[r][c+1]
        print(self.prefix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        oa = self.prefix[row1][col1]
        col_rec = self.prefix[row2+1][col1]
        row_rec = self.prefix[row1][col2+1]
        big_rec = self.prefix[row2 + 1][col2 + 1]
        print(oa, col_rec, row_rec,big_rec)
        return big_rec - col_rec - row_rec + oa
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)