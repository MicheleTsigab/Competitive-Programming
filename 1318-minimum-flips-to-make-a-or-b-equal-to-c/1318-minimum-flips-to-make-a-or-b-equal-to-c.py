class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(32):
            ax = 1&(a>>i)
            bx = 1&(b>>i)
            cx = 1&(c>>i)
   #         print(ax,bx,cx)
            if ax | bx != cx:
                if cx == 1:
                    ans += 1
                elif cx == 0:
                    ans += ax + bx
        return ans