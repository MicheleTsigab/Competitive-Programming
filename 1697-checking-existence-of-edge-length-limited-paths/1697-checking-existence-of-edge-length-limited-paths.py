class UnionFind:
    def __init__(self, size: int):
        self.group = [0] * size
        self.rank = [0] * size
        for i in range(size):
            self.group[i] = i

    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def join(self, node1: int, node2: int):
        group1 = self.find(node1)
        group2 = self.find(node2)
        
        # node1 and node2 already belong to same group.
        if group1 == group2:
            return

        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1
    
    def are_connected(self, node1: int, node2: int) -> bool:
        return self.find(node1) == self.find(node2)

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        unionfind = UnionFind(n)
        queries_count = len(queries)
        ans = [False] * queries_count
        q_i = []
        for i in range(queries_count):
            q_i.append(queries[i])
            q_i[i].append(i) #add orginal index
        q_i.sort(key =lambda k:k[2])
        edgeList.sort(key = lambda k:k[2])
        edge_index = 0
        for p,q,limit,orig_index in q_i:
            while edge_index < len(edgeList) and edgeList[edge_index][2] < limit:
                node1 = edgeList[edge_index][0]
                node2 = edgeList[edge_index][1]
                unionfind.join(node1,node2)
                edge_index += 1
            ans[orig_index] = unionfind.are_connected(p, q)
        return ans