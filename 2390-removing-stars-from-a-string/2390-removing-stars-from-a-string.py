class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for c in s:
            if c!='*':
                st.append(c)
                continue
            if st:
                st.pop()
        return ''.join(st)
        