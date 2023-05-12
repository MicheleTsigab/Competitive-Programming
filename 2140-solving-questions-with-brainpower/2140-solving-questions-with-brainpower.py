class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        dp = [-1] * len(questions)
        def search(i):
            if i >= len(questions):
                return 0
            if dp[i]!=-1:
                return dp[i]
            dp[i] = max(questions[i][0] + search(i+questions[i][1] + 1), search(i+1))
            return dp[i]
        return search(0)
