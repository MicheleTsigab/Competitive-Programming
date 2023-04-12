class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        """
        112358
        
        
        length
        1
        i = 0
        1 11 112 1123 11235 112358
        i = 1
    1   12 123 1235 12358
    i = 2
2 23 235 2358

        """
        found = False
        def search(i,path):
            nonlocal found
            if len(path) >= 3:
                if path[-1] != (path[-2] + path[-3]):
                    return False
            if i == len(num):

                good = False    
                for x in range(2,len(path)):
                    if path[x] == (path[x-1] + path[x-2]):
                        good = True
                    else:
                        break

                return good
            for j in range(i,len(num)):
                new = num[i:j+1]
                
                if len(new) > 1 and new[0]=='0':
                    continue
                path.append(int(new))
                if search(j+1,path):
                    return True
                path.pop()
            return False
                
        for i in range(len(num)):
            c = num[:i+1]
            if len(c) > 1 and num[0]=='0':
                return False
            if search(i+1,[int(c)]):
                return True
        return found