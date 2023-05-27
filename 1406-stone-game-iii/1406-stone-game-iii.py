class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        p = sum(stoneValue)
        @cache
        def solve(i,alice):
            if i >= len(stoneValue):
                return 0
            N = len(stoneValue)
            x = sum(stoneValue[i:min(i+1,N)]) - solve(i+1,not alice)
            y = sum(stoneValue[i:min(i+2,N)]) - solve(i+2,not alice)
            z = sum(stoneValue[i:min(i+3,N)]) - solve(i+3,not alice)
            return max(x,y,z)
        ans = solve(0,True) 
       # print(ans)
        if ans==0:
            return 'Tie'
        elif ans > 0:
            return 'Alice'
        return 'Bob'