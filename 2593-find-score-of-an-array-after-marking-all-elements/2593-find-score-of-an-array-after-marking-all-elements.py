class Solution:
    def findScore(self, nums: List[int]) -> int:
        x = sorted([(n,i) for i,n in enumerate(nums)])
        count = 0
        seen =set()
        for n,i in x:
            if i not in seen:
           #     print(n,i)
                seen.add(i)
                count+=n
                seen.add(i+1)
                seen.add(i-1)
        return count
                