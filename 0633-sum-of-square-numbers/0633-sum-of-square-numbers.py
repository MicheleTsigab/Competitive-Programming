class Solution:
    def judgeSquareSum(self, c: int) -> bool:        
        left = 0
        right = floor(sqrt(c))
        while left <= right:
            c1 = left * left + left * left
            c2 = right * right + right * right
            c3 = left * left + right*right
            if c1==c or c2==c or c3==c:
                return True
            elif c3 > c:
                right -=1
            elif c3 < c:
                left +=1
        return False
