class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = dict()
        def dfs(node):
            ans = True
            for neighbour in graph[node]:
                    if neighbour in color:
                        if color[neighbour] == color[node]:
                            ans = False
                            break

                    else:
                        color[neighbour] = not color[node]
                        if not dfs(neighbour):
                            return False
            return ans
        ans = True
        for i in range(len(graph)):
            if i not in color:
                color[i] = True
                ans = ans and  dfs(i)
        return ans