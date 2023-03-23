class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = [-1] * len(intervals)
        x = sorted([(n,i) for i,n in enumerate(intervals)],key = lambda a: a[0][0])
        
        for i in range(len(intervals)):
            _,endi = intervals[i]
            l = 0
            r = len(intervals) - 1
            while l <= r:
                m = l + (r-l)//2
                if x[m][0][0] >= endi:
                    ans[i] = x[m][1]
                    r = m - 1
                else:
                    l = m + 1
        return ans