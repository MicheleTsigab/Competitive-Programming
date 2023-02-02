class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        total = sum(matchsticks)
        sides = [0,0,0,0]
        target = total // 4
        if total % 4 !=0 or not matchsticks:
            return False
        def search(i=0):
            if i==len(matchsticks):
                return True
            for side in range(4):
                new_len = sides[side] + matchsticks[i]
                if new_len <= target:
                    sides[side]=new_len
                    if search(i+1):
                        return True
                    sides[side]-=matchsticks[i]
            return False
        return search()


            
        
        
