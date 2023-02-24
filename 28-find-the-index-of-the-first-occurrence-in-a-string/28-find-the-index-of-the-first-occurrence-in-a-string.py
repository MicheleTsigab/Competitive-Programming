class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for hay in range(len(haystack) - len(needle) + 1):
            if haystack[hay:hay + len(needle)]==needle:
                return hay
        return -1