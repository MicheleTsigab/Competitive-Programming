class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        x = sorted([(n[0],i) for i,n in enumerate(intervals)])
        ans = []
        for start,end in intervals:
            index = bisect_left(x, (end,))
            if index < len(intervals):
                ans.append(x[index][1])
            else:
                ans.append(-1)
        return ans