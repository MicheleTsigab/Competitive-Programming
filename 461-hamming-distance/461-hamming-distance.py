class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x or y:
            if (x & 1) ^ (y & 1):
                
                #print(x,y)
                ans+=1 
            #print(bin(x),bin(y))
            if x:
                x>>=1
            if y:
                y>>=1
        return ans