class Solution:
    def simplifyPath(self, path: str) -> str:
        st = ['/']
        m = path.split('/')
        #print(m)
        for i in range(len(m)):
            p = m[i]
            if p=='' or p=='.':
                continue
            if p=='..':
                if len(st) > 1:
                    st.pop()
                    st.pop()
                continue
            st.append(p)
            if i!=len(m)-1:
           #     print('')
                st.append('/')
        result = []
        result.append('/')
        # for i,n in enumerate(st):
        #     result.append(n)
        #     if i!=len(st)-1:
        #         result.append('/')
        if len(st) > 1 and st[-1]=='/':
            st.pop()
        return ''.join(st)