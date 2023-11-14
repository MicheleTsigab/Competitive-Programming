class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def can(i,am):

            if am == 0:
                return 1
            if am < 0 or i >= len(coins):
                return 0
            if (i,am) in dp:
                return dp[(i,am)]
            ans = can(i,am-coins[i-1]) + can(i+1,am)
            dp[(i,am)] = ans
            return ans
        return can(0,amount)