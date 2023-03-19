class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        seen = set()
        rows = len(grid[0])
        cols = len(grid[0])
        total = (rows * cols) - 1
        r,c = 0,0
        count = 0
        dirs = [[1,2],[-1,2],[-1,-2],[1,-2], [2,1],[-2,1],[-2,-1],[2,-1]]
        while count<total:
            if (r,c) in seen:
                break
            seen.add((r,c))
            for dx, dy in dirs:
                if 0 <= (r+dx) < rows and 0<=(c+dy)<cols and (r+dx,c+dy) not in seen:
                    if grid[r+dx][c+dy]==(count + 1):
                        count+=1
                        r= r + dx
                        c = c + dy
                        break
                        
            if count == total:                
                break
        return count == total