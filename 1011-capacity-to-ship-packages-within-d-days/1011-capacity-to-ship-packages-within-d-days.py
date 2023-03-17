class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        [1,2,3,4,5,6,7,8,9,10], days = 5
         0 1 2 3 4 5 6 7 8 9
         sum(weights) ---ship them in one day
         0 
        """
        #binary search
        l = 1
        r = sum(weights)
        ans = math.inf
        while l<=r:
            mid = l + (r - l)//2
            if self.possible(mid,weights,days):
                r = mid - 1
               # print(ans)
                ans = min(ans,mid)
            else:
                l = mid + 1
        return ans
                
    def possible(self,cap,weights,days):
        count = 0
        total = 0
        
        for i in range(len(weights)): 
            
            if weights[i] > cap:
                return False
            if weights[i] + total > cap:
                count +=1
                total = 0
            
            total += weights[i]
        if total:
            count += 1
        if count > days:
            return False
        return True