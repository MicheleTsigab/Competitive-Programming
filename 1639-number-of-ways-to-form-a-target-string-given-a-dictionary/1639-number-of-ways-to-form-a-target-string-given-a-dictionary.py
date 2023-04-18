class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        char_idx = defaultdict(int)
        mod = 10**9 + 7
        for w in words:
            for j,c in enumerate(w):
                char_idx[(j,c)] += 1
                
        cache = {} #target_idx,word_idx == to number of ways we can form
        
        def dfs(tar_idx,word_idx):
            if tar_idx == len(target):
                return 1
            if word_idx == len(words[0]):
                return 0
            if (tar_idx,word_idx) in cache:
                return cache[(tar_idx,word_idx)]
            
            cache[(tar_idx, word_idx)] = dfs(tar_idx, word_idx + 1)
            needed = target[tar_idx]
            cache[(tar_idx,word_idx)] += (
                char_idx[(word_idx,needed)] * dfs(tar_idx + 1, word_idx + 1)
            )
            return cache[(tar_idx, word_idx)] % mod

        return dfs(0,0)