class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = -math.inf
        force_right = [n for _ in range(len(dominoes))]
        force_left = [n for _ in range(len(dominoes))]
        
        #calculate force to the right
        for i,d in enumerate(dominoes):
            if d=='R':
                force_right[i] = 1
            elif d=='L':
                force_right[i] = n
            elif i-1 >= 0 and force_right[i-1]!=n:
                force_right[i] = force_right[i-1]-1
        
        #calculate force to the left start from right_most
        for i in range(len(dominoes)-1,-1,-1):
            d = dominoes[i]
            if d=='L':
                force_left[i] = 1
            elif d=='R':
                force_left[i] = n
            elif i+1 < len(dominoes) and force_left[i+1]!=n:
                force_left[i] = force_left[i+1]-1
        
        ans = [i for i in dominoes]

        for i in range(len(dominoes)):
            if dominoes[i]!='.':
                continue
            if force_right[i] > force_left[i]:
                ans[i] = 'R'
            elif force_left[i] > force_right[i]:
                ans[i]='L'
        return ''.join(ans)