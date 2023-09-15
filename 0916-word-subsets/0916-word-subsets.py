class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        w2 = Counter()
        for i in words2:
            freq = Counter(i)
            for k,v in freq.items():
                w2[k] = max(v,w2[k])
        ans = []
        for w in words1:
            f = Counter(w)
            flag = True
            for k,v in w2.items():
                if f[k] < v:
                    flag = False
                    break
            if flag:
                ans.append(w)
        return ans