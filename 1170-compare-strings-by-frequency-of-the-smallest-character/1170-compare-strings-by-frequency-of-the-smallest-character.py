class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        word_lex= [0]*len(words)
        for i,n in enumerate(words):
            word_lex[i] = n.count(sorted(n)[0])
        word_lex.sort()        
        ans = []
        length = len(word_lex)
        for q in queries:
            freq_small = q.count(sorted(q)[0])
            size = length - min(length,bisect_right(word_lex,freq_small))
            ans.append(size)
        return ans