class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh +=1
        minute = 0
        if not fresh:
            return 0
        visited = set()
        while q:
            
            
            if not fresh:
                return minute
            minute += 1
            for _ in range(len(q)):
                r,c = q.popleft()
                dirs =[[0,1],[1,0],[-1,0],[0,-1]]
                for dr,dc in dirs:
                    rn = dr + r
                    cn = dc + c
                    if (0 <= rn < rows and 0 <= cn < cols and 
                        grid[rn][cn] == 1 and (rn,cn) not in visited):
                        fresh -=1
                        if not fresh:
                            return minute
                        visited.add((rn,cn))
                        q.append((rn,cn))
            
            
            
        if fresh:
            return -1