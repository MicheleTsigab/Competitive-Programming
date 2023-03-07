class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        p = [0]*len(s) #prefix sum array
        for end, shift in enumerate(shifts):
            p[0]+=shift
            if end + 1 < len(s):
                p[end+1] -=shift
        ans = []
        for i in range(len(p)):
            if i > 0:
                p[i] += p[i-1]
            char = ((ord(s[i]) + p[i] - 97) % 26) + 97
            ans.append(chr(char))

        
        
        return ''.join(ans)