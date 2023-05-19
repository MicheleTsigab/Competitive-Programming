class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
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
        for i in range(1,n+1):
            if i not in color:
                color[i] = True
                ans =ans and dfs(i)
        return ans