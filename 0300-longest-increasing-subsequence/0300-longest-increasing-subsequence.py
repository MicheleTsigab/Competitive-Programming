class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        piles = []
        
        for n in nums:
            idx = bisect_left(piles,n)
            if idx == len(piles):
                piles.append(n)
            else:
             #   print(piles,idx)
                piles[idx] = n
       # print(piles)
        return len(piles)