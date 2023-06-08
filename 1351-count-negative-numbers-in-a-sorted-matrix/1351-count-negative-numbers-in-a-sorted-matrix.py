class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            l = 0
            r = len(grid[0])-1
            ans = len(grid[0])
            while l<=r:
                mid = l + (r-l)//2
                if grid[i][mid] >= 0:
                    l = mid + 1
                else:
                    
                    ans = min(ans,mid)
                    r = mid - 1
           
        #print(ans)
            res += len(grid[0]) - ans
        return res