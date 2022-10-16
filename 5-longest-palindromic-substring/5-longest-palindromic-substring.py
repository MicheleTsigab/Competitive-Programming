class Solution:
    def longestPalindrome(self, s: str) -> str:
        start=0
        end=0
        dp=[[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            dp[i][i]=True
            # if i-1>=0:
            #     if s[i]==s[i-1]:
            #         dp[i-1][i]=1
            #         start=i-1
            #         end=i
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    if j-i==1 or dp[i+1][j-1]:
                        dp[i][j]=True
                        if j-i>=end-start:#if length is greater than current update pointers
                            start=i
                            end=j
        return s[start:end+1]
     