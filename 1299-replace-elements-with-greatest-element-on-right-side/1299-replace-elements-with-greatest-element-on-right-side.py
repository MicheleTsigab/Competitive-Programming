class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        res = [-1] * len(arr)
        cur_max = arr[-1]
        for i in range(len(arr)-2,-1,-1):
            res[i] = cur_max
            cur_max = max(cur_max,arr[i])
        return res