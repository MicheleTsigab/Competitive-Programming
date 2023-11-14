class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)
        @lru_cache(1000)
        def dfs(i):
            if i>days[len(days)-1]:
                return 0
            if i not in days_set:
                return dfs(i+1)
            return min(costs[0]+dfs(i+1),
                       costs[1]+dfs(i+7),
                       costs[2]+dfs(i+30))
        return dfs(0)