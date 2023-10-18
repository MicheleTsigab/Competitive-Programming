class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        self.cache=dict()
    def addWord(self, word: str) -> None:
        curr=self.root
        for i in word:
            if i not in curr.children:
                curr.children[i]=TrieNode()
            curr=curr.children[i]
        curr.end=True
        self.cache.clear()

    def search(self, word: str) -> bool:
        curr=self.root
        # my task
        # b.., .b. find its match
        def dfs(count,root):
            curr=root
            for i in range(count,len(word)):
                if word[i]=='.':
                    for c in curr.children.values():
                        if dfs(i+1,c):
                            return True
                    return False
                if word[i] not in curr.children:
                    return False        
                curr=curr.children[word[i]]
            return curr.end
        if word in self.cache:
            return self.cache[word]
        #else search and cache
        if dfs(0,curr):
            self.cache[word]=True
            return True
        self.cache[word]=False
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)