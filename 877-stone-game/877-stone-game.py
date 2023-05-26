class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        winner = [0,0]
        def min_max(i,j,alice):
            if i>j:
                return 0
            x= piles[i] + min_max(i+1,j,not alice)
            y=piles[j]+min_max(i,j-1,not alice)
            if alice:
                return max(x,y)
            
            else:
                return -min(x,y)
        return min_max(0,0,True) > 0