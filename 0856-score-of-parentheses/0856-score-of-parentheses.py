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
                
                count += st.pop() + max(count,1)
                
        return count