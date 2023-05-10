class Solution:
    def countPrimes(self, n: int) -> int:
        x = [-1 for i in range(n)]
        
        for i in range(2,n):
            if x[i] == -1:
                j = i + i
                while j <n:
                    x[j] = 1
                    j+=i
     #   print(x)
        cnt = 0
        for i in range(2,len(x)):
            if x[i] == -1:
                cnt+=1
        return cnt