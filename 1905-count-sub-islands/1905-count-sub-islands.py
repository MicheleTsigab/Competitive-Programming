class Solution:
    def countSubIslands(self,grid1,grid2) -> int:
        rows,cols=len(grid1),len(grid2[0])
        visited=set()
        subisland=0
        def bfs(row,col):
            q=collections.deque()
            q.append((row,col))
            visited.add((row,col))
            marker=True
            while q:
                row,col=q.popleft()
                directions=[[-1,0],[1,0],[0,1],[0,-1]]
                for dx,dy in directions:
                    if ((row+dx) in range(rows) and
                       (col+dy) in range(cols) and
                       grid2[row+dx][col+dy]==1 and 
                        (row+dx,col+dy) not in visited):
                            q.append((row+dx,col+dy))
                            visited.add((row+dx,col+dy))
                            if grid1[row+dx][col+dy]!=1:
                                marker=False
            return marker
                        
        for row in range(rows):
            for col in range(cols):
                if (grid2[row][col]==1 and 
                    grid1[row][col]==1  and 
                   (row,col) not in visited
                   
                   ):
                    if bfs(row,col):
                        subisland+=1
        return subisland