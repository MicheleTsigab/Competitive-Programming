class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        g = defaultdict(list)
        for i in range(len(equations)):
            u,v = equations[i]
            g[u].append([v,values[i]])
            g[v].append([u,1/values[i]])
            
        def bfs(s,end):
            visited = set()
            visited.add(s)
            q = deque()
            q.append([s,1])
            while q:
                node,value = q.popleft()
                if node == end:
                    return value
                for nei,val in g[node]:
                    if nei not in visited:
                        q.append([nei,val * value])
                        visited.add(nei)
            return -1
        ans = []
        for u,v in queries:
            if u in g and v in g:
                ans.append(bfs(u,v))
            else:
                ans.append(-1)
        return ans