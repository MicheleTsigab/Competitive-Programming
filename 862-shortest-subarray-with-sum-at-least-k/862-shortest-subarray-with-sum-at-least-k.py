class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        left = 0
        total = 0
        result = math.inf
        inc_queue = deque() #monotonic increasing 
        for right,n in enumerate(nums):
            total +=n
            #total starting from 0 to right
            if total >=k:
                result=min(result,right+1)

            #if current window is greater than k we try to minimize the window by popping from left
            # we pop and maintain
            cur=-1
            while inc_queue and (total - inc_queue[0][0]) >=k:
                cur = inc_queue[0][1]
                inc_queue.popleft()
                

            if cur!=-1:
                result=min(result,right-cur)
            
            #maintain a monotonically increasing queue
            while inc_queue and total <= inc_queue[-1][0] :
                inc_queue.pop()
            
            inc_queue.append((total,right))
            
        return -1 if result==math.inf else result