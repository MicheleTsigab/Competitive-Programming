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
            temp = 0
            if copy == -1:
                temp = 2 + search(str_len * 2,str_len)
            else:
                temp = 1 + search(str_len + copy,copy)
            return min(temp,ans)
        return search(1,-1)