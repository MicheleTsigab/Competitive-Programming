class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        char_idx = defaultdict(int)
        mod = 10**9 + 7
        for w in words:
            for j,c in enumerate(w):
                char_idx[(j,c)] += 1
        
        
        @lru_cache(None)
        def dfs(tar_idx,word_idx):
            if tar_idx == len(target):
                return 1
            if word_idx == len(words[0]):
                return 0
            
            # choosing next index
            res = dfs(tar_idx, word_idx + 1)
            needed = target[tar_idx]
            if char_idx[(word_idx, needed)]: #there is a match
                res += (
                    char_idx[(word_idx,needed)] * dfs(tar_idx + 1, word_idx + 1)
                )
 
            return res % mod
        return dfs(0,0)