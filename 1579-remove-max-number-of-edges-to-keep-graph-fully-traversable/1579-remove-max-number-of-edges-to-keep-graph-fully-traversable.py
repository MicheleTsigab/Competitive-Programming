class UnionFind:
    def __init__(self,n):
        self.components = n
        self.rep = [i for i in range(n+1)]
        self.comp_size = [ i for i in range(n+1)]
    def findRep(self,node):
        if self.rep[node] == node:
            return node
        
        #path compression
        self.rep[node] = self.findRep(self.rep[node])
        return self.rep[node]
    
    def performUnion(self,x,y):
        x = self.findRep(x)
        y = self.findRep(y)
        
        #same group
        if x == y:
            return 0
        if self.comp_size[x] > self.comp_size[y]:
            self.comp_size[x] += self.comp_size[y]
            self.rep[y] = x
        else:
            self.comp_size[y] += self.comp_size[x]
            self.rep[x] = y
        self.components -= 1
        return 1
    def isConnected(self):
        return self.components == 1
        
        
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        
        edge_req = 0
        
        for edge in edges:
            if edge[0] == 3:
                edge_req += max(alice.performUnion(edge[1],edge[2]),bob.performUnion(edge[1],edge[2]))
                
        for edge in edges:
            if edge[0] == 1:
                edge_req += alice.performUnion(edge[1],edge[2])
            elif edge[0] == 2:
                edge_req += bob.performUnion(edge[1],edge[2])
        
        if alice.isConnected() and bob.isConnected():
        #    print('here')
            return len(edges) - edge_req
        return -1