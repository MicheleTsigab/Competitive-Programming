class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        r = 0
        l = 0
        if len(haystack) < len(needle):
            return -1
        while l < len(haystack):
            r = l
            i = 0
            while r < len(haystack) and i < len(needle) and haystack[r]==needle[i]:
                r+=1
                i+=1
            if i==len(needle):
                return l
            l+=1
        return -1