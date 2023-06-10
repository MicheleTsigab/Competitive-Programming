class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        [4,2,7,6,9,14,12]
           i
         j = - 5 - 3 5 -
            3
         [5] 
        """
        hl = [] #min heap
        ans = 0
        for i in range(1,len(heights)):
            ans = i
            if heights[i] <= heights[i-1]:
                continue
            diff = heights[i]-heights[i-1]
            heapq.heappush(hl,diff)
            #length of current diffs > available ladders
            while hl and len(hl) > ladders:
                x = heapq.heappop(hl)
                if x > bricks:
                    return i -1
                bricks-=x
      #  print(ans,hl)
        return ans
    