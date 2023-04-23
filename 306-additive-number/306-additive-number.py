class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        @lru_cache(None)
        def search(i,path):
            if len(path) >= 3:
                if path[-1] != (path[-2] + path[-3]):
                    return False
            if i == len(num) and len(path) >= 3:
                return True
            for j in range(i,len(num)):
                new = num[i:j+1]

                if len(new) > 1 and new[0] == '0':
                    continue
                x = int(new)
                if not path:
                    temp = (x,)
                elif len(path) >= 2:
                    temp = (path[-2],path[-1],x)
                else:
                    temp = (path[-1],x)
                    
                if search(j+1,temp):
                    return True
            return False
        
        return search(0,())
        