class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        piles = []
        for n in nums:
            idx = bisect_left(piles,n)
            if idx == len(piles):
                piles.append(n)
            else:
                piles[idx] = n
            if len(piles) == 3:
                return True
        return False