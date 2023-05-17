class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = [0] * (len(edges)+1)
        for u,v in edges:
            degree[u-1]+=1
            degree[v-1]+=1
            if degree[u-1] == len(edges):
                return u
            if degree[v-1] == len(edges):
                return v
        