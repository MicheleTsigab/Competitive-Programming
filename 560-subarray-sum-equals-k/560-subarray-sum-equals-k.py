class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre={}
        pre[0]=1
        sump=0
        res=0
        for i in nums:
            sump+=i
            temp=sump-k
            if temp in pre:
                res+=pre[temp]
            pre[sump]=pre.get(sump,0)+1
        return res