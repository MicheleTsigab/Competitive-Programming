class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1

        graph = {edge:[] for edge in range(n)}
        
        for i,j in connections:
            graph[i].append(j)
            graph[j].append(i)
        visited = set()
        
        def search(node):
            component = 1
            visited.add(node)
            
            for g in graph[node]:
                if g in visited:
                    continue
                visited.add(g)
                component+=search(g)
            return component
                
        count = 0
        for i in range(n):
            if i not in visited:
                search(i)
                count+=1

        return count - 1