class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        p = [0]*len(s) #prefix sum array
        for end, shift in enumerate(shifts):
            p[0]+=shift
            if end + 1 < len(s):
                p[end+1] -=shift

        for i in range(1,len(p)):
            p[i] += p[i-1]

        ans = []
        for i in range(len(s)):
            char = ((ord(s[i]) + p[i] - 97) % 26) + 97
            ans.append(chr(char))
        
        return ''.join(ans)