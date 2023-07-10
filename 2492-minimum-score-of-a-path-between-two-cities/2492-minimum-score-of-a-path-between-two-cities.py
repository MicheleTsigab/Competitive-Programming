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
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        cost = [math.inf]*(n+1)
        dsu = UnionFind(n+1)
        for a,b,d in roads:
            dsu.union(a,b)
            p1 = dsu.find(a)
            p2 = dsu.find(b)
            cost[p1]= min(cost[p1],d)
            cost[p2]=min(cost[p2],d)
        p1 = dsu.find(1)
        p2 = dsu.find(n)
        #print(cost)
        ans = math.inf
        for i in range(1,n+1):
            x= dsu.find(i)
    #        if i == 12:
     #           print(x,p1,p2,cost[12])

            if x==p1 or x==p2:
                ans = min(cost[i],ans)
        return ans