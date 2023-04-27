class Solution:
    def bulbSwitch(self, n: int) -> int:
        ans = 0
        for i in range(1,n+1):
            temp = i * i
            if temp > n:
                break
            ans += 1
        return ans
            
        