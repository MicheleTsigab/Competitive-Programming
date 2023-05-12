class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @lru_cache(None)
        def search(i):
            if i >= len(questions):
                return 0
            return max(questions[i][0] + search(i+questions[i][1] + 1), search(i+1))
        return search(0)