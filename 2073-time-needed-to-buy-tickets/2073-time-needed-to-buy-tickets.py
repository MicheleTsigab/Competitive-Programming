class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = k
        q = deque([(tick, i) for i,tick in enumerate(tickets)])
        time = 0
        while tickets[k]:
         #   print(q)
            t,i = q.popleft()
            
            if t:
                t-=1
                if t:
                    q.append((t,i))
           
            tickets[i] = t
            time +=1
        return time