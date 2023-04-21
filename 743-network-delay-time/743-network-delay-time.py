class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        seen = set()    
        pq = [(0,k)] #pq[0] represent total time to reach it from node k
        ans = 0
        while pq:
            w1,v1 = heapq.heappop(pq)
            if v1 in seen:
                continue
            seen.add(v1)
            ans = max(ans, w1)
            
            for v2, w2 in graph[v1]:
                if v2 not in seen:
                    heapq.heappush(pq,(w2 + w1,v2))
        return ans if len(seen) == n else -1