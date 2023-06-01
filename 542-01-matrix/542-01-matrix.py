class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        rows = len(mat)
        cols = len(mat[0])
        ones = 0
        ans = []
        for i in range(rows):
            temp = []
            for j in range(cols):
                temp.append(0)
                if mat[i][j] == 0:
                    q.append([i,j])
                else:
                    ones+=1
            ans.append(temp)
        l = 0
        seen = set()
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        while q:
            l+=1
            for _ in range(len(q)):
                r,c = q.popleft()
                seen.add((r,c))
                
                for dr,dc in dirs:
                    rn = dr + r
                    cn = dc + c
                    if 0<=rn<rows and 0<=cn<cols and (rn,cn) not in seen and mat[rn][cn] == 1:
                        ans[rn][cn] = l
                        q.append([rn,cn])
                        seen.add((rn,cn))
            
        return ans