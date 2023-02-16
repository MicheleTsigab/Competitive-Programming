class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        cur = ''        
        for word in dictionary: 
            found= self.longest(word,s)
            if not found:
                continue
    
            #compare to find longest
            if len(word) > len(cur):
                cur = word

            #if tie(same length) choose lexicographically smaller one
            elif len(word)==len(cur):
                cur = min(word,cur)
        return cur
    
    def longest(self,target,s): #O(len(target))
        """
        return True if target is a subsequence of s
        """
        count,pointer_t,pointer_s = 0,0,0
        while pointer_t < len(target) and pointer_s < len(s):
            if s[pointer_s]==target[pointer_t]:
                count +=1
                pointer_t +=1
                pointer_s +=1
            else:
                pointer_s +=1
        return count==len(target)
    #N = len(dictionary)
    #X = average length of the words in dictionary
    #O(NXlogN + XN)
    #improved
    #O(NX)