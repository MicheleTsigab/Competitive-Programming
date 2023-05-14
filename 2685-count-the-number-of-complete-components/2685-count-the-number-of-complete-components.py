class Dsu:
    def __init__(self,n):
        self.comp_count = n
        self.parent = [i for i in range(n)]
        self.components = [1 for i in range(n)]
    def find(self,node):
        if self.parent[node] == node:
        	return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self,n1,n2):
        root1 = self.find(n1)
        root2 = self.find(n2)
        if root1 == root2:
            return 0
        if self.components[root1] > self.components[root2]:
            self.components[root1]+=self.components[root2]
            self.components[root2] = 0
            self.parent[root2] = root1
        else:
            self.components[root2]+=self.components[root1]
            self.components[root1] = 0
            self.parent[root1] = root2
        self.comp_count -=1
        return 1
    def num_comp(self):
        return self.comp_count
            
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = Dsu(n)
        edge_set = set()
        for x,y in edges:
            graph.union(x,y)
            edge_set.add((x,y))
            edge_set.add((y,x))
        discard = set()
        cnt = graph.num_comp()
        for i in range(n):
            for j in range(i+1,n):
                root1 = graph.find(i)
                root2 = graph.find(j)
                if root1 == root2 and (i,j) not in edge_set:
                    if root1 in discard:
                        continue
                    cnt -=1
                    discard.add(root1)
        return cnt
                    