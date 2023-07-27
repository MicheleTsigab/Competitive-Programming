class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = [[1]]
        for i in range(1,numRows):
            level = []
            level.append(1)
            #process
            for j in range(i-1):
                x =ans[-1][j] + ans[-1][j+1]
                level.append(x)
            level.append(1)
            ans.append(level)
        return ans