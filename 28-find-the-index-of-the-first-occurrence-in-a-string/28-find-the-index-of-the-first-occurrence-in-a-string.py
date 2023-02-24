class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for hay in range(len(haystack) - len(needle) + 1):
            pointer_n = 0
            while pointer_n < len(needle) and haystack[hay]==needle[pointer_n]:
                hay+=1
                pointer_n+=1
            if pointer_n == len(needle):
                return hay - pointer_n
        return -1