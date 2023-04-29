class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = defaultdict(int)
        seen = set()
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 0:
                return 0
            seen.add((r,c))
            dirs = [(0,1),(1,0),(-1,0),(0,-1)]
            res = grid[r][c]
            for dr,dc in dirs:
                ro = r + dr
                co = c + dc
                if (ro,co) not in seen:
                    res+=dfs(ro,co)
            return res
        ans = 0
        for r in range(rows):
            for c in range(cols):
                x = 0
                if (r,c) not in seen:
                    ans = max(ans,dfs(r,c))
        #print(dp)
        return ans