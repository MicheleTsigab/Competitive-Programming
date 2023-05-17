class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        def peri(r,c):
            ans = 0
          #  print(r,c,'here')
            if r+1 >= rows or grid[r+1][c] == 0:
                ans+=1
            if c+ 1 >= cols or grid[r][c+1] == 0:
                ans+=1
            if c - 1 < 0 or grid[r][c-1]==0:
                ans+=1
            if r-1 < 0 or grid[r-1][c] == 0:
                ans +=1
         #   print(ans)
            return ans
        ans = 0
        def search(r,c):
            nonlocal ans
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == 0:
                return 0
            visited.add((r,c))
            dirs = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr,dc in dirs:
                ry = dr + r
                cx = dc + c
                if 0<=ry < rows and 0<=cx < cols and (ry,cx) not in visited and grid[ry][cx]==1:
                    ans += peri(ry,cx)
                    search(ry,cx)
                    
            return ans
                    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    ans+=peri(r,c)
                    search(r,c)
                    break
        return ans
