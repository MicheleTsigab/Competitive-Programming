class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s)-1
        delete = 0
        while l < r and s[l]==s[r]:
            comp = s[r]
            while s[l]==comp and l<r:
                l+=1
            while s[r]==comp and r>=l:
                r-=1
        return r-l+1