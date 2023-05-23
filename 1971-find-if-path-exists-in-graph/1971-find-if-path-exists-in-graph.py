class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited =set()
        def bfs(start):
            q = deque()
            q.append(start)
            visited.add(start)
            
            while q:
                node = q.popleft()
                if node == destination:
                    return True
                for nei in graph[node]:
                    if nei not in visited:

                        visited.add(nei)
                        q.append(nei)
            return False
        return bfs(source)
                        
                        