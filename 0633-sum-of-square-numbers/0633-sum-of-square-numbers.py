class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        r = ceil(sqrt(c))
        l = 0

        while l <= r:
            tar =l*l + r*r 
            if tar > c:
                r-=1
            elif tar < c:
                l+=1
            else:
                return True
        return False
