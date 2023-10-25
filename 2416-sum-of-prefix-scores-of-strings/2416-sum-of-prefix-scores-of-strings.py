class Trie:
    def __init__(self):
        self.ch = {}
        self.seen = 0
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        ans = []
        
        for word in words:
            t = trie
            for c in word:
                if c not in t.ch:
                    t.ch[c]= Trie()
                t.ch[c].seen+=1
                t = t.ch[c]
        for word in words:
            t,curr = trie,0
            for c in word:
                curr += t.ch[c].seen
                t = t.ch[c]
            ans.append(curr)
        return ans