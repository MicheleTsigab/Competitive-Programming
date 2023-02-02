class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:            
        bucket = [0] * (1001)
        for num in arr1:
            bucket[num] += 1
        res = []
        for num in arr2:
            res.extend(bucket[num] * [num])
            bucket[num] = 0

        for i, n in enumerate(bucket):
            if n:
                res.extend([i] * n)
        return res
        
            