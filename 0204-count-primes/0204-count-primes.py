class Solution:
    def countPrimes(self, n: int) -> int:
        x = [-1 for i in range(n)]
        i = 2
        while i * i < n:
            if x[i] == -1:
                j = i + i
                while j <n:
                    x[j] = 1
                    j+=i
            i+=1
     #   print(x)
        cnt = 0
        for i in range(2,len(x)):
            if x[i] == -1:
                cnt+=1
        return cnt