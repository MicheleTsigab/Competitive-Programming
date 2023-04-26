class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        arr = [3,1,2,4]
                 i
        st = 0
        """
        total = 0
        inc_st = []
        mod = 10**9 + 7
        for i in range(len(arr)+1):
            
            while inc_st and (i == len(arr) or arr[inc_st[-1]] > arr[i]):
                idx = inc_st.pop()
                r_boundary = i
                l_boundary = inc_st[-1] if inc_st else -1
                width = (idx - l_boundary) * (r_boundary - idx)
                total += width * arr[idx]
            
            inc_st.append(i)
        
        return total % mod