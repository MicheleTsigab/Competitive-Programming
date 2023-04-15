class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = {}
        def cal_max(pile_idx,coins):
            """
            given parameters i-denoting which pile we are at and coins which tells us how much coins we have got so far, calculate max for each position
            """
            
            if pile_idx == len(piles):
                return 0
            if (pile_idx, coins) in dp:
                return dp[(pile_idx, coins)]

            
            dp[(pile_idx,coins)] = cal_max(pile_idx + 1, coins)
            cur_pile = 0
            for j in range(min(coins,len(piles[pile_idx]))):
                cur_pile += piles[pile_idx][j] 
                dp[(pile_idx,coins)] = (max(dp[(pile_idx,coins)], 
                         cur_pile + cal_max(pile_idx + 1, coins - j - 1))
                                       )
            return dp[(pile_idx,coins)]

        return cal_max(0,k)
            