class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        total = sum(matchsticks)
        target = total // 4
        if total % 4 != 0:
            return False
        res =[]
        answer = [False]
        def search(sides, i,cur_sum):
            if answer[0] or cur_sum==total:
                answer[0] = True
                return
            if i >=len(matchsticks):
                return
            for side in range(4):
                new_len = sides[side] + matchsticks[i]
                if new_len <= target:
                    sides[side]=new_len
                    search(sides, i+1,cur_sum + matchsticks[i])
                    sides[side]-=matchsticks[i]
        search([0,0,0,0],0,0)
        return answer[0]


            
        
        
