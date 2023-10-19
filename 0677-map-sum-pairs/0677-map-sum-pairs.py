class TrieNode:
    def __init__(self):
        self.children={}
        self.score=0
class Trie:

    def __init__(self):
        self.root=TrieNode()

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.kmap = {}
        
    def insert(self, key: str, val: int) -> None:
        #calculate prefix score for each node
        delta = val - self.kmap.get(key,0)
        self.kmap[key] = val
        cur = self.root
        for char in key:
            if char not in cur.children:
                cur.children[char]=TrieNode()
            cur = cur.children[char]
            cur.score += delta
                

        

    def sum(self, prefix: str) -> int:
        curr=self.root
        for i in prefix:
            if i not in curr.children:
                return 0
            curr=curr.children[i]
        return curr.score


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)