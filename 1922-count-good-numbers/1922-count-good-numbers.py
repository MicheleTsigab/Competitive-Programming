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
        mod = 10**9 + 7
        if n==0:
            return 5
        if n%2==0:
            return (pow(5*4,n//2,mod))%(10**9 + 7)
        else:
            return 5 * pow(20,(n - 1)//2,mod)%(10**9 + 7)
        