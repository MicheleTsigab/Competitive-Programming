class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """
        4,3, 3,1 1,2
        0 1 2 3 4 5 6 7 8 9 10
        p p p p g g g b
                p g g b 
                  p p p g b
        """
        pair = sorted(zip(growTime,plantTime),reverse=True)
        ans = 0
        prev_plant = 0
        for g,p in pair:
            ans = max(ans, prev_plant + p + g)
            prev_plant += p
        return ans