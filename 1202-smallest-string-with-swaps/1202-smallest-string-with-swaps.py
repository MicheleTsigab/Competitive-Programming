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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = UnionFind(len(s))
        for i,j in pairs:
            dsu.union(i,j)
        gangs = defaultdict(list)
        for c in range(len(s)):
            par = dsu.find(c)
            gangs[par].append(s[c])
        for i in gangs.keys():
            gangs[i].sort(reverse=True)
        ans = []
        for c in range(len(s)):
            par = dsu.find(c)
            ans.append(gangs[par].pop())
        return ''.join(ans)
        
        
                