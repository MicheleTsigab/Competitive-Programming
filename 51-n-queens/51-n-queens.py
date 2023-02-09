class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        [q... .... .... ....]
        """
        res = []
        curr = [['.' for i in range(n)] for j in range(n)]
        
        def place(i):
            if i==n:
                x = [''.join(i) for i in curr]
                res.append(x)
            for row in range(i,n):
                for col in range(n):
                    if curr[row][col]=='.':
                        if self.isvalid(curr,row,col):
                            curr[row][col]='Q'
                            place(row+1)
                            curr[row][col]='.'
                    else:
                        break
                return
        place(0)
        return res
    
    def isvalid(self,board,row,col):
        n= len(board[0])
        for i in range(n):
            if board[row][i]=='Q':
                return False
            if board[i][col]=='Q':
                return False
            for j in range(n):
                if board[i][j]=='Q' and abs(row - i)==abs(col-j):
                    return False
        return True
        