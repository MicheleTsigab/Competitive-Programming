class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size
       # self.comp = 0
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([dist,i,j])
        edges.sort()
        n = len(points)
        uf = UnionFind(n*n)
        ans = 0
        for ed in edges:
            pa1= uf.union(ed[1],ed[2])
            if pa1:
                ans += ed[0]
        return ans
        