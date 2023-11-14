class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(1000)
        def dfs(i,j):
            if j==len(t):
                return 1
            if i>=len(s):
                return 0
            if s[i]==t[j]:
                return dfs(1+i,1+j) + dfs(1+i,j)
            return dfs(1+i,j)
        return dfs(0,0)