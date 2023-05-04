class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)
        
        
        while r and d:
            r_i = r.popleft()
            d_i = d.popleft()
            if r_i < d_i:
                r.append(r_i + len(senate))
            else:
                d.append(d_i + len(senate))
        if len(r):
            return 'Radiant'
        return 'Dire'
        
                