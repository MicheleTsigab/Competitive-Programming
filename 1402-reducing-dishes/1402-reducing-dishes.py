class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        @lru_cache(None)
        def solve(i,t):
            if i >= len(satisfaction):
                return 0
            return max(satisfaction[i]*t+solve(i+1,t+1),solve(i+1,t))
        return solve(0,1)