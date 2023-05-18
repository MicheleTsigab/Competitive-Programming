class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = dict()
        def dfs(node):
            for neighbour in graph[node]:
                    if neighbour in color:
                        if color[neighbour] == color[node]:
                            return False

                    else:
                        color[neighbour] = not color[node]
                        if not dfs(neighbour):
                            return False
            return True
        ans = True
        for i in range(len(graph)):
            if i not in color:
                color[i] = True
                ans = ans and  dfs(i)
        return ans