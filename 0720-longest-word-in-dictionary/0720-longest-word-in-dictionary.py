class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False
class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        curr=self.root
        for i in word:
            if i not in curr.children:
                curr.children[i]=TrieNode()
            curr=curr.children[i]
        curr.end=True
    def validate(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if not curr.children[i].end:
                return False
            curr = curr.children[i]
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        #get which words can be made one character at a time
        ans = ''
        for w in words:
            if trie.validate(w):
                if len(ans) < len(w):
                    ans = w
               # ans.append(w)
        return ans