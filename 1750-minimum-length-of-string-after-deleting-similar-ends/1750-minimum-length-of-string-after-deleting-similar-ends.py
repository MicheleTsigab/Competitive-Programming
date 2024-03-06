class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s)-1
        delete = 0
        while l < r and s[l]==s[r]:
            right = s[r]
            left = s[l]
            while s[l]==right and l<r:
                delete+=1
                l+=1
            while s[r]==left and r>=l:
                delete+=1
                r-=1
   #     print(s[l],s[r],l,r)
        return len(s)-delete