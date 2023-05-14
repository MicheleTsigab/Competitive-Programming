class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        seen = set()
        i = 0
        j = 1
        while i not in seen:
            seen.add(i)
            i += j * k
            i %= n
            j+=1
        res = []
        for i in range(n):
            if i not in seen:
                res.append(i+1)
        return res
            