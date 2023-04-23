class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
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
                    
                path.append(int(new))
                if search(j+1,path):
                    return True
                path.pop()
            return False
        
        return search(0,[])
        