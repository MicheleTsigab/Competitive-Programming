class Solution:
    def splitString(self, s: str) -> bool:
        found = [False]
        def search(i,prev):
            if i==len(s):
                return True
            for j in range(i,len(s)): 
                #find next substring starting next to i, e.g if given 0, check
                # 5, 50, 500, 5004, 500043
                curr = int(s[i:j+1])
                if prev - curr == 1 and search(j+1,curr):
                    return True
            return False
        for i in range(len(s)-1): #find specific prev value of starting from index 0
            #e.g 0, 05, 050, 0500, 05004
            value= int(s[:i+1])
            if search(i+1,value):
                return True
        return False
