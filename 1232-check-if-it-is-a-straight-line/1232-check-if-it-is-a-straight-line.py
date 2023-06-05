class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1 = coordinates[1]
        x2,y2 = coordinates[0]
        if x2 - x1 == 0:
            m = None
        else:
            m = (y2 - y1)/(x2-x1)
            b = y1 - (x1 * m)
        for x,y in coordinates:
            if m == None:
                if x != x1:
                    return False
                continue
            if y!=m*x + b:
                return False
        return True