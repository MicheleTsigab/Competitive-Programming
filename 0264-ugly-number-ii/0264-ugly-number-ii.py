class Solution:
    def nthUglyNumber(self, n: int) -> int:
        #2,3,5
        if n==1:
            return 1
        min_heap = [1]
        for i in range(1,n):
            x = heappop(min_heap)
            while min_heap and min_heap[0]== x:
                heappop(min_heap)
            for i in [2,3,5]:
                heappush(min_heap,i*x)
                n-=1

#        print(min_heap)
        return min_heap[0]