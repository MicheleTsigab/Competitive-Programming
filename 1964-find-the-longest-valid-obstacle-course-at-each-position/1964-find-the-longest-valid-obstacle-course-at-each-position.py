class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        """
        1 4 5 8 9 17 2 5 0 2 3
        
        1 4 5 8 9 17 
        0 2 5  
          2 3
        """
        piles = []
        ans = []
        for n in obstacles:
            idx = bisect_right(piles,n)
    #        print(idx)
            if idx == len(piles):
                piles.append(n)
            else:
                piles[idx] = n
            ans.append(idx+1)
        return ans