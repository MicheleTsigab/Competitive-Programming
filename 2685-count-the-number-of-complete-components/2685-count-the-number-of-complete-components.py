class Dsu:
    def __init__(self,n):
        self.comp_count = n
        self.parent = [i for i in range(n)]
        self.components = [1 for i in range(n)]
        self.edges = [0 for i in range(n)]
    def find(self,node):
        if self.parent[node] == node:
        	return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self,n1,n2):

        root1 = self.find(n1)
        root2 = self.find(n2)
        self.edges[root1]+=1
        if root1 == root2:
            return 0

        self.components[root1]+=self.components[root2]
        self.edges[root1]+=self.edges[root2]
        self.parent[root2] = root1
        self.comp_count -=1
        return 1
    def num_complete(self):
        ans = 0
        n = len(self.components)
        for i in range(n):
            if self.find(i) == i:
                x = self.components[i]
                if self.edges[i] ==  (x * (x-1)//2):
                    ans += 1
        return ans

            
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = Dsu(n)
        for x,y in edges:
            graph.union(x,y)

        return graph.num_complete()
                    