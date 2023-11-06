class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[0 for i in range(len(s)+1)]
        dp[0]=1
        dp[1]=1 if int(s[0]) else 0
        for i in range(2,len(s)+1):
            one=int(s[i-1])
            two=int(s[i-2:i])
            if 1<=one<=26:
                dp[i]+=dp[i-1]
            if 10<=two<=26:
                dp[i]+=dp[i-2]
        return dp[-1]
                    
                
                