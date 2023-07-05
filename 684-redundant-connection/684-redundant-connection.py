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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        s = set()
        for i,j in edges:
            s.add(i)
            s.add(j)
        uf = UnionFind(len(s))
        for i,j in edges:
            if not uf.union(i-1,j-1): #already in union
              #  if uf.cap(uf.find(i-1)) == len(s):
                return i,j