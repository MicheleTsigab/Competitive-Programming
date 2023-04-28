class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        edge = defaultdict(list)
        pairs = set()
        for i,word in enumerate(strs):
            for j in range(i,len(strs)):
                if self.similar(strs[j],word):
                    if (word,strs[j]) not in pairs or (strs[j],word) not in pairs:
                        pairs.add((word,strs[j]))
                        edge[strs[j]].append(word)
                        edge[word].append(strs[j])
        seen = set()
        def dfs(node):
            seen.add(node)
            for nei in edge[node]:
                if nei not in seen:
                    dfs(nei)
        ans = 0
        for i in strs:
            if i not in seen:
                ans  += 1
                dfs(i)
        return ans
    
    def similar(self,word1,word2):
        count = 0
        for i in range(len(word1)):
            if word1[i]!=word2[i]:
                count += 1
            if count > 2:
                return False
        return True