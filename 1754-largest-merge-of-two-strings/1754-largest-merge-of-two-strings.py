class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        w1_p = 0
        w2_p = 0
        merge = []
        while w1_p < len(word1) and w2_p < len(word2):
            if word1[w1_p] > word2[w2_p]:
                merge.append(word1[w1_p])
                w1_p +=1
            elif word2[w2_p] > word1[w1_p]:
                merge.append(word2[w2_p])
                w2_p +=1
            else:
                if word1[w1_p:] > word2[w2_p:]: #look forward
                    merge.append(word1[w1_p])
                    w1_p += 1
                else:
                    merge.append(word2[w2_p])
                    w2_p += 1
        while w1_p < len(word1):
            merge.append(word1[w1_p])
            w1_p += 1
        while w2_p < len(word2):
            merge.append(word2[w2_p])
            w2_p += 1
        return ''.join(merge)