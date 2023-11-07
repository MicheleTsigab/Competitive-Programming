class Solution:
    def countSubstrings(self, s: str) -> int:
        start=0
        end=0
        count=0
        dp=[[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            dp[i][i]=True
            count+=1
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    if j-i==1 or dp[i+1][j-1]:
                        dp[i][j]=True
                        count+=1
        return count