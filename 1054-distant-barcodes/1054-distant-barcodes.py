class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        """
         [1,1,1,2,2,2]
         1: 3
         2: 3
          0,1,2,3,4,5,6,7
         [1,0,1,0,1,0,1,0]
         
         i=0
                p       s
        """
        count = Counter(barcodes)
        pq = [(-v,n) for n,v in count.items()]
        heapq.heapify(pq)
        result =[0] * len(barcodes)
        k = 0
        length = len(barcodes)
        prev_count=1
        i = 0
        while k < len(barcodes):
            c,n = heapq.heappop(pq)
            for _ in range(abs(c)):
                if i >= length:
                    i = length
                    i = (i % length) + prev_count
                    prev_count+=1
                result[i]=n
                i+=2
                k+=1
            
        return result