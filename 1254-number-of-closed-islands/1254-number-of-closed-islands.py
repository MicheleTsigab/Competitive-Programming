class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        seen = set()
        def search(r,c):
            if (r < 0 or c < 0 or
                r == rows or c == cols):
                return 0
            if grid[r][c] == 1 or (r,c) in seen:
                return 1
            seen.add((r,c))
            found = min(search(r+1,c),
                     search(r-1,c),
                     search(r,c+1),
                     search(r,c-1)
                    )
            return found
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if not grid[i][j] and (i,j) not in seen:
                    count+=search(i,j)
                        #count +=1
        return count
                    