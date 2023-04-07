class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        seen = set()
        temp = 0
        def dfs(r,c):
            nonlocal temp
            if (r < 0 or c < 0 or
               c == cols or r == rows):
                return False
            if grid[r][c] == 0 or (r,c) in seen:
                return True
            seen.add((r,c))
            temp+=1
            up = dfs(r-1,c)
            down = dfs(r+1,c)
            right = dfs(r,c+1)
            left = dfs(r,c-1)
            
            return up and down and right and left
                        
        
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    if dfs(r,c):
                        count += temp
                    temp = 0
        print(seen)
        return count