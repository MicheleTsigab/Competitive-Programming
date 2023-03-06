class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1freq=Counter(s1)
        win=Counter(s2[:len(s1)])
        start=''
        end=''
        if win==s1freq:
            return True
        for i in range(len(s1),len(s2)):
            start=s2[i-len(s1)]
            end=s2[i]
            win[end]+=1
            if win[start]!=0: 
                win[start]-=1
            if win==s1freq: 
                return True
        return False
