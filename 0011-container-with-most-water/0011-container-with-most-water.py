class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0 , len(height) -1
        area = lambda l,h : l*h
        max_area = 0
        while left < right:
            l = right - left
            h = min(height[left],height[right])
            cur_area = area(l, h)
            max_area = max(cur_area, max_area)
            if height[left] > height[right]:
                right -=1
            else:
                left +=1
        return max_area