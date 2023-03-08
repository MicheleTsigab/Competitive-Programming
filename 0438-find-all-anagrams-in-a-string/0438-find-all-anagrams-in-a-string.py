class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        s1freq=Counter(p)
        
        #first window
        win=Counter(s[:len(p)])
        sol=[]
        if win==s1freq:
            sol.append(0)
        
        left = 0
        for right in range(len(p),len(s)):
            char = s[right]
            win[char]+=1
            
            char_left = s[left]
            win[char_left]-=1
            if win[char_left]==0:
                del win[char_left]
            
            left +=1
            if win==s1freq:
                sol.append(left)
        return sol