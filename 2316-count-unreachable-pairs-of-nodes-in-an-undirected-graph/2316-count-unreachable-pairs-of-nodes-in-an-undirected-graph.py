class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = {edge:[] for edge in range(n)}
        
        for i,j in edges:
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
        rn = n #remaining nodes
        for i in range(n):
            if i not in visited:
                component = search(i)
                count += component * (rn - component)
                rn -= component

        return count