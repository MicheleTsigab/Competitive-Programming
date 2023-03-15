class Solution:
    def countGoodNumbers(self, n: int) -> int:
        """
        n = 4
        5 4 5 4 5 4
        (5*4)**3
        0 1 2 3
        even = 5
        prime = 4
        """
        def power(x,n,mod):
            if n==0:
                return 1
            if n==1:
                return x%mod
            if n%2==0:
                return power(x%mod*x%mod,n//2,mod)%mod
            else:
                return (x%mod)*power(x%mod*x%mod,n//2,mod)%mod

        mod = 10**9 + 7
        if n==0:
            return 5
        ans = (power(5*4,n//2,mod))%(mod)
        if n%2==0:
            return ans
        
        return (5 * ans)%mod
        