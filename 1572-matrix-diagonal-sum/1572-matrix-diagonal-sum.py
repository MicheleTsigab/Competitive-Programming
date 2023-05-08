class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        [
        [7,3,1,9],
        [3,4,6,9],
        [6,9,6,6],
        [9,5,8,5]]

        """
        ans = 0
        rows = len(mat)
        for i in range(rows):
            ans+=mat[i][i]
            ans+=mat[i][rows-i-1]
        if rows % 2:
            ans-=mat[rows//2][rows//2]
        return ans