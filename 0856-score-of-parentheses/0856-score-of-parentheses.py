class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        (( () )) ()
                  i
        count = st.pop() + max(count,1)
        st = [ ]
        count = 0

        """
        st = []
        count = 0
        for c in s:
            if c == '(':
                st.append(count)
                count = 0
            else:
                temp = st.pop() if st else 0
                count += temp + max(count,1)
                
        return count