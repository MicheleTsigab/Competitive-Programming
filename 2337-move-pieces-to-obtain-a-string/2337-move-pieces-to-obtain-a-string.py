class Solution:
    def canChange(self, start: str, target: str) -> bool:
        """
        __R_  __R_
        """
        if target.count("_")!=start.count("_"):
            return False
        s,t = 0,0
        ans = True
        while s < len(start)  and t < len(target):
            while s < len(start)-1 and start[s]=="_":
                s+=1
            while t < len(target)-1 and target[t]=="_":
                t+=1
            #print(s,t,)
            #three case
            if target[t]!= start[s]:
                return False
            else:#equal
                if s > t and target[t]=='R':
                    return False
                elif s < t and target[t]=='L':
                    return False
                ans = ans and True
            s+=1
            t+=1
            
        return ans
                