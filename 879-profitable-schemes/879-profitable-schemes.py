class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = (10 **9) + 7
        @lru_cache(None)
        def dfs(n,p,i):
            if i == len(group):
                return 1 if  p >= minProfit else 0

            res =  dfs(n,p,i+1)
            if n - group[i] >= 0:
                res += dfs(n - group[i],min(minProfit,p + profit[i]), i + 1)
            return res % mod
        return dfs(n,0,0)