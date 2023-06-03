class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rebel = set()
        rows = len(board)
        cols = len(board[0])

        for i in range(len(board[0])):
            if board[0][i] == 'O':
                rebel.add((0,i))
            if board[-1][i] =='O':
                rebel.add((rows-1,i))

        for j in range(len(board)):
            if board[j][0]=='O':
                rebel.add((j,0))
            if board[j][-1]=='O':
                rebel.add((j,cols-1))
        q = deque()
        for i in rebel:
            q.append(i)
        dirs  = [[1,0],[0,1],[0,-1],[-1,0]]
        seen = set()
        while q:
            r,c = q.popleft()
            if (r,c) not in seen:
                seen.add((r,c))
            for dy,dx in dirs:
                rn = dy + r
                cn = dx + c
                if 0<=rn<rows and 0<=cn<cols and (rn,cn) not in seen and board[rn][cn]=='O':
                    q.append((rn,cn))
                    seen.add((rn,cn))
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in seen:
                    board[r][c]='X'
            