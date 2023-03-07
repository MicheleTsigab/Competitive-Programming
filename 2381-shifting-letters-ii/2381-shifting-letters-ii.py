class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        p = [0]*len(s)
        for l,r,d in shifts:
            if d:
                p[l]+=1
                if r + 1 < len(s):
                    p[r+1] -=1
            else:
                p[l]-=1
                if r + 1 < len(s):
                    p[r+1]+= 1
        for i in range(1,len(p)):
            p[i] += p[i-1]
        ans = []
        for i in range(len(p)):
            char = ((ord(s[i]) + p[i] - 97) % 26) + 97
            ans.append(chr(char))
        
        return ''.join(ans)
    