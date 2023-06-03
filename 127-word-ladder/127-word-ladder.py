class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(i for i in wordList)
        q = deque()
        q.append([beginWord,1])
        seen = set()
        seen.add(beginWord)
        while q:
            node,leng = q.popleft()
            if node == endWord:
                return leng
            for i in range(len(node)):
                for c in string.ascii_lowercase:
                    nei = list(node)
                    nei[i] = c
                    nei = ''.join(nei)
                    if nei not in seen and nei in wordList:
                        q.append([nei,leng+1])
                        seen.add(nei)
        return 0