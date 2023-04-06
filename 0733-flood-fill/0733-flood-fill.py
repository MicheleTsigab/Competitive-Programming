class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows, cols = len(image), len(image[0])
        seen = set()
        def dfs(r,c,col):
            if (r < 0 or c < 0 or
               r >= rows or c >= cols):
                return
            
            if (r,c) not in seen and image[r][c] == col:
                seen.add((r,c))
                image[r][c] = color
                dfs(r+1,c,col)
                dfs(r-1,c,col)
                dfs(r,c-1,col)
                dfs(r,c+1,col)
        dfs(sr,sc,image[sr][sc])
        return image