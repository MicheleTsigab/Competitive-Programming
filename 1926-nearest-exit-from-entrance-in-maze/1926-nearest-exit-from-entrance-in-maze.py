class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        rows = len(maze)
        cols = len(maze[0])
        exit = set()
        for i in range(cols):
            if [rows-1,i]!=entrance and maze[rows-1][i]=='.':
                exit.add((rows-1,i))
            if [0,i]!=entrance and maze[0][i]=='.':
                exit.add((0,i))
        for i in range(rows):
            if [i,cols-1]!=entrance and maze[i][cols-1]=='.':
                exit.add((i,cols-1))
            if [i,0]!=entrance and maze[i][0]=='.':
                exit.add((i,0))
                
        q = deque()
        for i in exit:
            q.append(i)
        l = 0
        seen = set()
        while q:
            
            for _ in range(len(q)):
                r,c =q.popleft()
                if (r,c) not in seen:
                    seen.add((r,c))
                if [r,c] == entrance:
                    return l
                dirs = [[1,0],[0,1],[-1,0],[0,-1]]
                for dr,dc in dirs:
                    rn = dr + r
                    cn = dc + c
                    if 0<=rn<rows and 0<=cn<cols and (rn,cn) not in seen and maze[rn][cn]=='.':
                        q.append([rn,cn])
                        seen.add((rn,cn))
            l+=1
        return -1