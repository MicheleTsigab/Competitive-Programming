class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
            
            if rowIndex==0:
                return [1]
            
            prev = self.getRow(rowIndex - 1)
            result = [1]
            
            for i in range(1,rowIndex):
                result.append(prev[i] + prev[i-1])
                
            result.append(1)
            return result

        