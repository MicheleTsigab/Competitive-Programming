class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = []
        for l,r in zip(s,t):
            diff.append(abs(ord(l) - ord(r)))
        left = 0
        total = 0
        ans = 0
        for right in range(len(s)):
            total+= diff[right]
            while total > maxCost:
                total -= diff[left]
                left +=1
            ans = max(ans,right - left + 1)
        return ans