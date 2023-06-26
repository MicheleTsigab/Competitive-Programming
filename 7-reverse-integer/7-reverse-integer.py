class Solution:
    def reverse(self, x: int) -> int:
        digit=0
        if abs(x)==x:
            sign=1  
        else:
            sign=-1 
        n=abs(x)
        rev=0
        while(n>0):
            digit=n%10
            rev=10*rev+digit
            n=n//10
        rev=sign*rev
        return 0 if -2**31>rev or rev>2**31-1 else rev
 