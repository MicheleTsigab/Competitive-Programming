class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edge = defaultdict(list)

        for fro,to,p in flights:
            edge[fro].append([to,p])

        q = [[0,src,0]] #distance,node,weight
        path = [inf] * (n+1)
        while q:
            price,node,dist = heapq.heappop(q)

            if dist > k + 1 or dist > path[node]: #skip we have gotten a smaller path
                continue
            path[node] = dist
            if node == dst:
                return price

            for nei in edge[node]:
                heapq.heappush(q, [price + nei[1],nei[0],dist + 1])
        return -1