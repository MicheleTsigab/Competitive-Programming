class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        
        i = 0
        pu = 0
        while i < len(popped):
            if st and popped[i]==st[-1]:
                st.pop()
                i+=1
            else:
                if pu < len(pushed):
                    st.append(pushed[pu])
                    pu+=1
                else:
                    break
        return  i == len(popped)