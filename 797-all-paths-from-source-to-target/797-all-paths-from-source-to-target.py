class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        seen = [False]*n
        def dfs(node,path):
            path.append(node)
            seen[node]=True
            
            for nei in graph[node]:
                if not seen[nei]:
                    
                    dfs(nei,path)
                    
            seen[node] = False
            if node == n-1:
                ans.append(path.copy())
            path.pop()
        ans = []
        dfs(0,[])
        return ans