class Solution:
    def minInsertions(self, s: str) -> int:
        """
        leetcode
        i      j
        
        
        """
        @lru_cache(None)
        def dfs(i,j):
            if j >= len(s) or i < 0 or i >= j:
                return 0
            if s[i] == s[j]:
                return dfs(i+1,j-1)
            return min(1 + dfs(i,j-1),1 + dfs(i+1,j))
        return dfs(0,len(s)-1)