class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        rows = len(maze)
        cols = len(maze[0])
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        q = deque()
        seen = set()
        q.append([entrance[0],entrance[1],0])
        seen.add((entrance[0],entrance[1]))

        while q:
            r,c,dist =q.popleft()
            if [r,c]!=entrance and (r==0 or r == rows - 1 or c == 0 or c == cols-1):
                return dist

            for dr,dc in dirs:
                rn = dr + r
                cn = dc + c
                if 0<=rn<rows and 0<=cn<cols and (rn,cn) not in seen and maze[rn][cn]=='.':
                    q.append([rn,cn,dist+1])
                    seen.add((rn,cn))
        return -1