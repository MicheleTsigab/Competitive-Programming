class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        n = len(potions)
        for s in spells:
            idx = bisect_left(potions,ceil(success/s))
            ans.append(n-idx)
        return ans