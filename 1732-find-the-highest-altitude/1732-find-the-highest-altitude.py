class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        alt = 0
        for i in range(len(gain)):
            alt += gain[i]
        #    print(alt)
            ans = max(ans,alt)
        return ans