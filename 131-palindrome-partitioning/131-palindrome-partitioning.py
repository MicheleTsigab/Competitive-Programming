class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #  0 1 2
        # 0 t
        # 1  t 
        # 2    t
        #find valid palindrome and pre calculate it
        dp=[[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            dp[i][i]=True
        for i in range(len(s)-1,-1,-1): #2
            for j in range(i+1,len(s)): #
                if s[i]==s[j]:
                    if j-i==1 or dp[i+1][j-1]:
                        dp[i][j]=True
        #print(dp)
        result = []
        def search(index,curr):
            if index>=len(s):
                result.append(curr.copy())
                return
            for j in range(index,len(s)):
                if dp[index][j]:#palindrom
                    curr.append(s[index:j+1])
                    search(j+1,curr)
                    curr.pop()
        #for k in range(1,len(s)): #partition length
        search(0,[])
        return result