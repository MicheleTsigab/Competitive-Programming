class TrieNode:
    def __init__(self):
        self.ch={}
        self.idx=0
class WordFilter:

    def __init__(self, words: List[str]):
        self.t = TrieNode()        
        for idx,word in enumerate(words):
            for i in range(len(word)):
                cur = self.t
                cur.idx = idx
                suffix = word[i:]
                word_to_insert = suffix + '+' + word
                for c in word_to_insert:
                    if c not in cur.ch:
                        cur.ch[c]=TrieNode()
                    #print(cur[c])
                    cur.ch[c].idx = idx
                    cur = cur.ch[c]
                
                
    def f(self, pref: str, suff: str) -> int:
        cur = self.t
        for c in suff + '+' + pref:
            if c not in cur.ch:
                return -1
            cur = cur.ch[c]
        return cur.idx


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)