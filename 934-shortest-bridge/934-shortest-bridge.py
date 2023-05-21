class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r,c,comp):
            if r < 0 or r >= rows or c <0 or c >= cols:
                return
            visited.add((r,c))
            comp.add((r,c))
            dirs = [[0,-1],[0,1],[-1,0],[1,0]]
            for dr,dc in dirs:
                ry = dr + r
                cx = dc + c
                if 0<=cx<cols and 0<=ry<rows and grid[ry][cx]==1 and (ry,cx) not in visited:
                    dfs(ry,cx,comp)
        
        visited = set()
        one = set()
        two = set()
        first = False
        for i in range(rows):
            for j in range(rows):
                if (i,j) not in visited and grid[i][j]==1:
                    if not first:
                        dfs(i,j,one)
                        first = True
                    else:
                        dfs(i,j,two)
        ans = inf
        for p1 in one:
            for p2 in two:
                dist = abs(p2[0] - p1[0]) + abs(p2[1]-p1[1])
                if dist < ans: 
                    ans = dist

        return ans -1