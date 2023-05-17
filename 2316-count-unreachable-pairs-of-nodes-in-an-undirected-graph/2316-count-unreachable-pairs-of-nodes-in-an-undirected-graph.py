class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        seen = set()
        def dfs(node):
            seen.add(node)
            comp = 1
            for nei in graph[node]:
                if nei not in seen:
                    comp+=dfs(nei)
            return comp
        x = n
        ans = 0
        for i in range(n):
            if i not in seen:
                comp = dfs(i)
                rem = max(0,x - comp)
                ans += comp * rem
                x-=comp
        return ans
                