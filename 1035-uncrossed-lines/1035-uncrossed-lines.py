class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        

        @lru_cache(None)
        def dfs(i,j):
            if i == len(nums1) or j == len(nums2):
                return 0
            
            found = False
            k = j
            while k < len(nums2):
                if nums1[i] == nums2[k]:
                    found = True
                    break
                k+=1
            res = 0
            if found:
                res = 1 + dfs(i+1,k+1)
            res = max(res, dfs(i+1,j))
            return res
        return dfs(0,0)