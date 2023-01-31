class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        arr=[i for i in range(1,n+1)]
        def search(i,curr):
            if len(curr)==k:
                result.append(curr.copy())
                return
            if i >= len(arr):
                return
            curr.append(arr[i])
            search(i+1,curr)
            curr.pop()
            search(i+1,curr)
        search(0,[])
        return result