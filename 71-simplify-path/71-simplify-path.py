class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        m = path.split('/')
        #print(m)
        for i in range(len(m)):
            p = m[i]
            if p=='' or p=='.':
                continue
            if p=='..':
                if st:
                    st.pop()
                continue
            st.append(p)
        result = []
        result.append('/')
        for i,n in enumerate(st):
            result.append(n)
            if i!=len(st)-1:
                result.append('/')
        return ''.join(result)