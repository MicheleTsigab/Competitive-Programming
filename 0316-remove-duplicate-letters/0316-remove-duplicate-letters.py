class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        cb a cdcbc
                 i
        count = {c:3 b:1 a:1 d:1}
        inc = [acdb]
        
        if next-smaller and in dict:
        
        []
        acdb
        bacd
        cbad
        
        """
        count = Counter(s)
        inc_st = []
        inc_set =set()
        for c in s:
            
            while inc_st and c not in inc_set and c < inc_st[-1] and count[inc_st[-1]]!=0:
                
                x = inc_st.pop()
                inc_set.remove(x)
                
            count[c]-=1
            if c not in inc_set:
                inc_st.append(c)
                inc_set.add(c)
            #print(inc_st,inc_set)
        return ''.join(inc_st)
                
        