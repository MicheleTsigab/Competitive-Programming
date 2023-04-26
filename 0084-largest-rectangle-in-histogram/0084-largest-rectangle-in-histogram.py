class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        inc_st = []
        mod = 10**9 + 7
        for i in range(len(heights)+1):
            
            while inc_st and (i == len(heights) or heights[inc_st[-1]] > heights[i]):
                idx = inc_st.pop()
                r_boundary = i
                l_boundary = inc_st[-1] if inc_st else -1
                width = (idx - l_boundary) + (r_boundary - idx) -1
                max_area = max(max_area, width * heights[idx])
            
            inc_st.append(i)
        
        return max_area