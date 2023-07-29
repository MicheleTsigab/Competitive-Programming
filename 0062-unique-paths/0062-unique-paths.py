class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
#         if (m,n) in self.memo:
#             return self.memo[(m,n)]
        
#         else:
#             res=self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)
#             self.memo[(m,n)]=res
#             return res
#            (m+n-2)!/(m-1)!*(n-1)!
        # dp=[[0 for i in range(n)] for i in range(m)]
        # for i in range(n):
        #     dp[0][i]=1
        # for i in range(m):
        #     dp[i][0]=1
        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[i][j]=dp[i-1][j] + dp[i][j-1]
        # return dp[m-1][n-1]
        return int(math.factorial((m+n-2))/(math.factorial((m-1))*math.factorial((n-1))))