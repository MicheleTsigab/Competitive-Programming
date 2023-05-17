class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0]*n
        edge = set()
        for u,v in roads:
            edge.add((u,v))
            edge.add((v,u))
            degree[u]+=1
            degree[v]+=1
        ans = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                ans = max(ans, degree[i]+degree[j]- (1 if (i,j) in edge else 0))
        return ans