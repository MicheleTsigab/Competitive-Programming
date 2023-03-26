class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.winner = []
        
        votes = {i:0 for i in persons}
        for n in persons:
            votes[n]+=1
            if not self.winner or votes[n] >= votes[self.winner[-1]]: 
                self.winner.append(n)
                continue
            
            self.winner.append(self.winner[-1])
        del votes
    def q(self, t: int) -> int:
        idx = bisect_left(self.times,t)
        if idx == len(self.winner):
            return self.winner[-1]
        if self.times[idx]==t:
            return self.winner[idx]
        #print(t,self.winner,self.times,idx,self.winner[idx])
        return self.winner[max(0,idx-1)]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)