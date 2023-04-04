class Solution:
    def partitionString(self, s: str) -> int:
        
        seen = set()
        count = 1
        for i in s:
            if i in seen:
                seen.clear()
                count+=1
            
            seen.add(i)
        return count