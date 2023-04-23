class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        """
        1000
        1   10   100
       0   0 00  0 0
      0
     0
        """
        mod = 10 ** 9 + 7
        len_k = len(str(k))
        @lru_cache(None)
        def search(start): #starting index
            if start == len(s):
                return 1
            if s[start] == '0':
                return 0
            res = 0
            for end in range(start,len(s)):
                new = s[start:end+1]
                if int(new) > k:
                    break
                res += search(end+1)
                
            return res % mod
        
        return search(0) % mod