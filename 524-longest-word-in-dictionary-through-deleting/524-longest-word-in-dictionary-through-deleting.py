class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        res = ''
        
        for word in sorted(dictionary):
            x= self.longest(word,s)
            res = max(res,x , key= len)
        return res
    def longest(self,target,s):
        ans = []
        pointer_t = 0
        pointer_s = 0
        while pointer_t < len(target) and pointer_s < len(s):
            if s[pointer_s]==target[pointer_t]:
                ans.append(s[pointer_s])
                pointer_t +=1
                pointer_s +=1
            else:
                pointer_s +=1
        return ''.join(ans) if len(ans)==len(target) else ''