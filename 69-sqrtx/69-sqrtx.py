class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        ans=0
        high=x
        while high>=low:
            mid=low+(high-low)//2
            temp=mid*mid
            if temp==x:
                return int(mid)
            if temp>int(x):
                high=mid-1
            else:
                low=mid+1
                ans=mid
        return ans   