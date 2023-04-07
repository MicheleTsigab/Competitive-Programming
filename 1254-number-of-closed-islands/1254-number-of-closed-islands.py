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
            down = search(r+1,c)
            up = search(r-1,c)
            left = search(r,c-1)
            right = search(r,c+1)
            
            return up and down and left and right

        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if not grid[r][c] and (r,c) not in seen:
                    if search(r,c):
                        count += 1
        return count
                    