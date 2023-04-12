class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        """
        st = [-1]
        mx = 0
        for r,p in enumerate(s):
            if p=='(':
                st.append(r)
            else:
                if st:
                    st.pop()
                if not st:
                    st.append(r)
                mx = max(mx,r-st[-1])
        return mx