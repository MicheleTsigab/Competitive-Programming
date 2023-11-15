class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ranges = []
        for i in nums:
            ranges.append([i-k,i+k])
        ans = 1
        #print(ranges)
        for i in range(len(ranges)):
            _,end1 = ranges[i]
            left = i + 1
            right = len(ranges)-1
            found = -1
            while left <= right:
                mid = (left + right)//2

                if end1 in range(ranges[mid][0],ranges[mid][1]+1):
                    #answer found
                    found = max(found,mid)
                #    print(found,'hello')
                    left = mid + 1
                else:
                    right = mid - 1
            #print(found,i)
            if found!=-1:
                ans = max(found-i+1, ans)
        return ans
