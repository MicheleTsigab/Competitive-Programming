class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        cnt = 0
        for w in words:
            flag = 1
            for i in range(len(pref)):
                
                if i >= len(w) or pref[i]!=w[i]:
                  #  print(w,pref)
                    flag = 0
                    break
            cnt += flag
                
            
        return cnt