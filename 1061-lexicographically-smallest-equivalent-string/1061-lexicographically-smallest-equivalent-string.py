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
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        alphabet = string.ascii_lowercase
        alph_idx = {ch:i for i,ch in enumerate(alphabet)}
        dsu = UnionFind(len(alphabet))
        for i in range(len(s1)):
            dsu.union(alph_idx[s1[i]],alph_idx[s2[i]])
        ans = []
        for ch in baseStr:
            idx = alph_idx[ch]
            parent = dsu.find(idx)
            for pos in range(0,idx+1):
                if dsu.find(pos)==parent:
                    ans.append(alphabet[pos])
                    break
        return ''.join(ans)