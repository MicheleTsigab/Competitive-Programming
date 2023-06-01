class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for i in range(len(bombs)):
            x,y,r = bombs[i]
            for j in range(len(bombs)):
                if i == j:
                    continue
                x1,y1,r1 = bombs[j]
                if (r**2) >= ((x-x1)**2 + (y-y1)**2):
                    graph[i].append(j)
                    
        def bfs(i):
            q = deque()
            comp = 0
            q.append(i)
            seen.add(i)
            while q:
                n = q.popleft()
                comp +=1
                for nei in graph[n]:
                    if nei not in seen:
                        
                        q.append(nei)
                        seen.add(nei)
            return comp
                        

        seen = set()
        ans = 0
        for i in range(len(bombs)):
            seen = set()
            ans = max(ans,bfs(i))
        return ans