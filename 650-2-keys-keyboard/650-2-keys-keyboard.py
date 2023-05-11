class Solution:
    def minSteps(self, n: int) -> int:
        
        @lru_cache(None)
        def search(str_len,copy):
            if str_len == n:
                return 0
            if str_len > n:
                return inf
            
            #take choice one
            ans = 2 + search(str_len * 2,str_len)
            if copy!=-1:
                ans = min(ans, 1 + search(str_len + copy,copy))
            return ans
        return search(1,-1)