class UnionFind:
    def __init__(self, stone):
        self.root = {tuple(i):tuple(i) for i in stone}
 #       print(self.root)
        self.size = {tuple(i):1 for i in stone}
        self.num = len(stone)
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def components(self):
        return self.num
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        self.num -=1
        if self.size[rootX] > self.size[rootY]:
            self.root[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        else:
            self.root[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        return True
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stones.sort(key=lambda a:a[0])
        uf = UnionFind(stones)
        for i in range(1,len(stones)):
            if stones[i][0] !=stones[i-1][0]:
                continue
            uf.union((stones[i][0],stones[i][1]),(stones[i-1][0],stones[i-1][1]))
        #    print('here',i)
        stones.sort(key=lambda a:a[1])
        for i in range(1,len(stones)):
            if stones[i][1]!=stones[i-1][1]:
                continue
            uf.union((stones[i][0],stones[i][1]),(stones[i-1][0],stones[i-1][1]))
        return len(stones) - uf.components()