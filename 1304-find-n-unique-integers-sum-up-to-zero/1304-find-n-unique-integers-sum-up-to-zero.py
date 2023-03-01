class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [0] * n
        left = 0
        right = len(res) - 1
        n = 2*n
        while left < right:
            res[left] = n
            res[right] = -n
            n-=1
            left += 1
            right -= 1
        return res