class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        res = []
        for i in intervals:
            cur_start = i[0]
            cur_end = i[1]
            if not res or res[-1][1] < cur_start:
                res.append([cur_start,cur_end])
            else:
                res[-1][1]= max(cur_end, res[-1][1])
        return res
            
            