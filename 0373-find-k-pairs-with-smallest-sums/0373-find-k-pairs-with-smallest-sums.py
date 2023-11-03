class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        seen = set()
        seen.add((0,0))
        n = len(nums1)
        m = len(nums2)
        min_heap = [[nums1[0]+nums2[0],0,0]]
        ans = []
        i,j = 0,0
        while k and min_heap:
            sm,i,j = heappop(min_heap)
         #   print(sm,i,j)
            ans.append([nums1[i],nums2[j]])
            k-=1
            if i+1 < n and (i+1,j) not in seen:
                heappush(min_heap,[nums1[i+1]+nums2[j],i+1,j])
                seen.add((i+1,j))
                #k-=1
            if j+1 < m and (i,j+1) not in seen:
                heappush(min_heap,[nums1[i]+nums2[j+1],i,j+1])
                seen.add((i,j+1))
                #k-=1
        return ans