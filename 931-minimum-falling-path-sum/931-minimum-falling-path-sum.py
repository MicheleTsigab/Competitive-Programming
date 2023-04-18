class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        cache = {}
        
        def dfs(r,c):
            if r == len(matrix) or c < 0 or c == len(matrix[0]):
                return inf
            if (r,c) in cache:
                return cache[(r,c)]

            
            res = min(dfs(r+1,c+1), dfs(r+1,c), dfs(r+1,c-1))
            cache[(r,c)] = matrix[r][c] + (res if res!=inf else 0)
            
            return cache[(r,c)]
        
        answer = inf
        for i in range(len(matrix[0])):
            answer = min(answer,dfs(0,i))

        return answer