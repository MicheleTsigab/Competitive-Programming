class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        for i in s.split():
            ans.append(i[::-1])
        return ' '.join(ans)