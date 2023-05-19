class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for i in range(n)]
        for u,v in dislikes:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        def dfs(node):
            
            
            for nei in graph[node]:
                if (nei) in color:
                    if color[nei] == color[node]:
                        return False
                else:
                    color[nei] = not color[node]
                    if not dfs(nei):
                        return False
            return True
        
        ans = True
        color = dict()
        for i in range(n):
            if i not in color:
                color[i] = True
                ans =ans and dfs(i)
        return ans