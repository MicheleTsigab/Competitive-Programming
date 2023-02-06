class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        count = [0] * (24 * 60)
        for i in timePoints:
            hh,mm=[int(i) for i in i.split(":")]
            
            count[hh*60 + mm]+=1
        last_seen = -1
        min_diff = inf
        # compute seen max and min to calculate last edge case where the times are in frist and last
        # min_time = inf 
        # max_time = -inf
        count +=count
        for i in range(len(count)):
            if count[i]>1:
                return 0
            elif count[i]==1:
                # min_time = min(min_time,i)
                # max_time = max(max_time,i)
                if last_seen != -1:
                    min_diff= min(min_diff,i - last_seen)
                last_seen = i
        
        # min_diff= min(min_diff,24*60 - max_time + min_time)
        
        return min_diff