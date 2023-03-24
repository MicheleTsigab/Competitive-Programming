class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(i,j) for i,j in connections}
        graph = {city:[] for city in range(n)}
        visited = set()
        for i,j in connections:
            graph[i].append(j)
            graph[j].append(i)
        
        count = 0
        def search(city):
            nonlocal count,graph,visited
            for n in graph[city]:
                if n in visited:
                    continue
                if (n,city) not in edges:
                    count+=1
                visited.add(n)
                search(n)
        visited.add(0)
        search(0)
        return count