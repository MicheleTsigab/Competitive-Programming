class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        ans = []
        for i,n in enumerate(candies):
            ans.append(n + extraCandies >= m)
        return ans
                