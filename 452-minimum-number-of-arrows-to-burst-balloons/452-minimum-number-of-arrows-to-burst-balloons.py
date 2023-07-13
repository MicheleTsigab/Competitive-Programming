class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
    #              ___l_________
    #                   ________r___________ 
    #  _____________
    # ___________       
    # ______________________________________
    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16    
        points.sort(key=lambda i:i[0])
        #left_start = points[0][0]
        left_end = points[0][1]
        count = 0
        for i in range(1,len(points)):
            right_start = points[i][0]
            right_end = points[i][1]
            if left_end >= right_start: 
                if left_end >= right_end: 
                # if left overlaps
                # and our left end is also bigger than right end, we take right variab
                #because we want minimum arrow to shoot
                    left_start = right_start
                    left_end = right_end
            else: #if they don't overlap, we count and set the left pointer as well 
                count +=1
                left_start = right_start
                left_end = right_end
        return count + 1 #arrow for the last point