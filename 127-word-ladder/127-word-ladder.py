class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        q = deque()
        q.append([beginWord,1])
        seen = set()
        seen.add(beginWord)
        while q:
            node,leng = q.popleft()
            if node == endWord:
                return leng
            for j in range(len(wordList)):
                nei = wordList[j]
                if nei not in seen:
                    count = 0
                    for x,y in zip(node,wordList[j]):
                        if x!=y:
                            count +=1
                        if count >=2:
                            break
                    if count == 1:
                        q.append([nei,leng+1])
                        seen.add(nei)
        return 0