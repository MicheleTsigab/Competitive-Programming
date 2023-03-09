class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for i in logs:
            if i=='./':
                continue
            if i=='../':
                if count:
                    count-=1
            else:
                count+=1
        return count