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
    def equationsPossible(self, equations: List[str]) -> bool:
        n = 26
        equal = UnionFind(n)
        for i in equations:
            a = int(ord(i[0]) - ord('a'))
            b = int(ord(i[-1])-ord('a'))
            if i[1] == '=':
                equal.union(a,b)
        for i in equations:
            a = int(ord(i[0]) - ord('a'))
            b = int(ord(i[-1])-ord('a'))
            if i[1] == '!' and equal.find(a)==equal.find(b):
                return False
        return True
                