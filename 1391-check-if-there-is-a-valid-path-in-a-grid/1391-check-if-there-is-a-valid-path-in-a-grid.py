class UnionFind:
    def __init__(self,r,c):
        self.root ={}
        for i in range(r):
            for j in range(c):
                self.root[(i,j)]=(i,j)
        self.size =defaultdict(int)
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def cap(self,x):
        return self.size[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.size[rootX] > self.size[rootY]:
            self.root[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        else:
            self.root[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        return True
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        config = {1: [(0,-1),(0,1)],
                      2: [(-1,0),(1,0)],
                      3: [(0,-1),(1,0)],
                      4: [(0,1),(1,0)],
                      5: [(0,-1),(-1,0)],
                      6: [(0,1),(-1,0)]
                 }
        rows,cols = len(grid),len(grid[0])
        dsu = UnionFind(rows,cols)
        for r in range(rows):
            for c in range(cols):
                for dy,dx in config[grid[r][c]]:
                    rn = r + dy
                    cn = c + dx
                    if 0 <= rn < rows and 0 <= cn < cols and (-dy,-dx) in config[grid[rn][cn]]:
                        dsu.union((r,c),(rn,cn))
        p1 = dsu.find((0,0))
        p2 = dsu.find((rows-1,cols-1))
        if p1==p2:
            return True
        return False