class Solution:
    def simplifyPath(self, path: str) -> str:
        
        st = []
        for p in path:
            if not st or p!='/':
                st.append(p)
                continue                    
            if st and p=='/':
                if st and st[-1]=='/':
                    continue
                if len(st) > 2 and st[-1]=='.' and st[-2]=='.' and st[-3]=='/':
                    
                    st.pop() #.
                    st.pop() #.
                    if len(st)<=1: #already in base case
                        continue
                    else:
                        st.pop() #trailing /
                        
                    while st and st[-1]!='/': #moving up
                        st.pop()
                    continue
                        
                elif len(st) > 1 and st[-1]=='.' and st[-2]=='/':
                    st.pop() #.   
                else:
                    st.append(p)

        if len(st) > 2 and st[-1]=='.' and st[-2]=='.' and st[-3]=='/':
            st.pop()
            if st[-1]=='.':
                st.pop()
                if len(st)>1: #already in base case
                    st.pop() #trailing /
                    
                while st and st[-1]!='/': #moving up
                    st.pop()
        elif len(st) > 1 and st[-1]=='.' and st[-2]=='/':
            st.pop()
            
        
        if len(st) > 1 and st[-1]=='/':
            st.pop()
            
        return ''.join(st)