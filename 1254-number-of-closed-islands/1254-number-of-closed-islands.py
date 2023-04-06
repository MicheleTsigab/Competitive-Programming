class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        seen = set()
        def search(r,c):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols):
                return False
            if grid[r][c] == 1 or (r,c) in seen:
                return True
            seen.add((r,c))
            dirs = [(-1,0),(1,0),(0,1),(0,-1)]
            found = True
            for dy, dx in dirs:
                if not search(r + dy, c + dx):
                    found = False
            return found
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if not grid[i][j] and (i,j) not in seen:
                    if search(i,j):
                        count += 1
        return count
                    