class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = []
        for i in piles:
            h.append(-i)
        heapq.heapify(h)
        while h and k:
            x = heapq.heappop(h)
            x = -1*x
            k-=1
            if ceil(x/2) > 0:
                
                heapq.heappush(h,-1*ceil(x/2))
        ans = 0
        for i in h:
            ans += (-1*i)
        return ans