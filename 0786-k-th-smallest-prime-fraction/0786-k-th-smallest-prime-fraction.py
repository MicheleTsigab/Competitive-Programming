class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        h = []
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                x = arr[i]/arr[j]
             #   h.append(x)
                heapq.heappush(h,[-x,arr[i],arr[j]])
           #     print(h)
                if len(h) > k:
                    heapq.heappop(h)
        # print(h)
        # h.sort()
        # print(h)
        # return [0,0]
        return [h[0][1],h[0][2]]