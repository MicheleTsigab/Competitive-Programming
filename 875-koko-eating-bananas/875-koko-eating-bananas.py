class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # since len(piles) <= h, we can guarantee that eating max of piles will take len(piles) hours hence under h
        #1<--->max(piles)
        def hour(k):
            count = 0
            for i in piles:
                if k > i:
                    count +=1
                else:
                    rem = 1 if i%k else 0
                    count += i//k + rem
            return count
        x=hour(2)
        low,high = 1,max(piles) # range of bananas i can eat
        ans = max(piles)
        while low<=high:
            mid = low + (high - low)//2
            time = hour(mid)
            #print(time,mid)
            if time > h:
                low = mid + 1 
            else:
                ans = min(ans,mid)
                high = mid - 1
        return ans
        