class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        inc_stack=[] # monotonic increasing stack
        n=len(heights)
        next_smaller = [n] * n
        prev_smaller = [-1] * n
        for i,n in enumerate(heights):
            while inc_stack and heights[inc_stack[-1]] > n:
                index=inc_stack.pop()
                next_smaller[index]=i
            prev_smaller[i]= inc_stack[-1] if inc_stack else -1
            inc_stack.append(i)
        max_area = 0
        for i,n in enumerate(heights):
            width = (next_smaller[i] - prev_smaller[i]) - 1
            #print(n,width)
            area = width * n
            max_area=max(area,max_area)
        return max_area
            