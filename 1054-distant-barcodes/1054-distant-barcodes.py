class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        #O(n) approach
        count = [0] * (max(barcodes) + 1)
        num,freq = 0,0
        for i in barcodes:
            count[i] += 1
            if count[i] > freq:
                freq = count[i]
                num = i
        count[num] = 0 #
        length = len(barcodes)
        result =[0] * length
        cur_size,prev_count,i = 0,0,0
        
        while cur_size < length:
            c,n = freq, num #c - count of a number n
            num, freq = len(count) - 1, count.pop()
            for _ in range(abs(c)):
                if i >= length:
                    prev_count +=1
                    i = prev_count
                result[i]=n
                i+=2
                cur_size+=1
            
        return result
#o(nlogn) approach        
#         #frequency
#         count = Counter(barcodes)
        
#         #max heap to track which is the current most frequent element
#         pq = [(-v,n) for n,v in count.items()]
#         heapq.heapify(pq) 
#         length = len(barcodes)
#         result =[0] * length
#         cur_size,prev_count,i = 0,0,0
        
#         while cur_size < length:
#             c,n = heapq.heappop(pq) #c - count of a number n
#             for _ in range(abs(c)):
#                 if i >= length:
#                     prev_count +=1
#                     i = prev_count
#                 result[i]=n
#                 i+=2
#                 cur_size+=1
            
#         return result