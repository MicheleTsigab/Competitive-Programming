class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.num_comp = 0

    def make_set(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            self.num_comp +=1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.rank[root_y]+=self.rank[root_x]
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += self.rank[root_y]
            self.num_comp -=1
def get_factors(n):
    if n == 1:
        return [1]
    s = set()
    while n % 2 == 0:
        n = n//2
        s.add(2)

    for i in range(3,int(n**0.5)+1,2):
        while n % i == 0:
            n = n//i
            s.add(i)
    if n > 2:
        s.add(n)
    return list(s)
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        
        

        if len(nums)==1:
            return True
        for i in nums:
            if i == 1:
                return False
        dsu = DisjointSet()
        alone = set()
        checking = -1
        for n in nums:
            prime_fs= get_factors(n)
            if len(prime_fs)==1:
                dsu.make_set(prime_fs[0])
            for i in range(1,len(prime_fs)):
                dsu.make_set(prime_fs[i])
                dsu.make_set(prime_fs[i-1])
                dsu.union(prime_fs[i],prime_fs[i-1])
                checking = prime_fs[i]
        
        return dsu.num_comp == 1
            