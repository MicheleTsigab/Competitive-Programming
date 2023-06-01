class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        q = deque()
        if grid[0][0]==0:
            q.append([0,0,1])
        seen = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        seen[0][0] = True
        while q:
            r,c,l = q.popleft()
            if r + 1 == rows and c + 1 == cols:
                return l
            dirs = [[1,0],[0,1],[0,-1],[-1,0],[1,-1],[-1,1],[-1,-1],[1,1]]
            for dy,dx in dirs:
                #print(r,c)
                rn = dy + r
                cn = dx + c
                if 0 <= rn < rows and 0<=cn < cols and not seen[rn][cn] and grid[rn][cn]==0:
                    #print('here')
                    q.append([rn,cn,l+1])
                    seen[rn][cn] = True
        return -1
                    