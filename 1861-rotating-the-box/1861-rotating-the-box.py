class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rotated_box = self.rotate_without_gravity(box)
        rows = len(rotated_box)
        cols = len(rotated_box[0])
        print(rotated_box)
        #start from last row, check if gravity applies for the cell
        for r in range(rows-1,-1,-1):
            for c in range(0,cols):
                if rotated_box[r][c]!="#":
                    continue
                #print(r,c)
                i=r+1
                while i < rows and (rotated_box[i][c]=='.'):
                    #print('here',i,c)
                    i+=1
                if r < i - 1 < rows and rotated_box[i-1][c]=='.':
                    rotated_box[i-1][c],rotated_box[r][c] = rotated_box[r][c],rotated_box[i-1][c]
        return rotated_box
    
    def rotate_without_gravity(self, box):
        rows = len(box)
        cols = len(box[0])
        rotated_box = [[0 for i in range(rows)] for i in range(cols)]
        
        #transpose
        for row in range(rows):
            for col in range(cols):
                item = box[row][col]
                rotated_box[col][row] = item
        
        #reflect
        for i in rotated_box:
            i.reverse()
        return rotated_box
                