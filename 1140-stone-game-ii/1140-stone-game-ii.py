class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        @cache
        def min_max(j,m,alice):
            if j >= len(piles):
                return 0
            mx = -math.inf
            mn = math.inf
            res = -math.inf if alice else math.inf
            tot = 0
            for i in range(1,min(2*m,n-j)+1):
                tot += piles[i+j-1]
                x = tot + min_max(j+i,max(m,i),not alice)
                if alice:
                    res = max(x,res)
                else:
                    res = min(x-tot,res)
            return res
        return min_max(0,1,True)
        