class Solution:
    def findComplement(self, num: int) -> int:
        
        res = 0 #final answer
        i = 0 #which bit
        while num:
            if num & 1 == 0:
                res+= (1<<i)
            i+=1
            num>>=1
        return res