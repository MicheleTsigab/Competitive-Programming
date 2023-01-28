class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums: #o(n)
            freq[i]=freq.get(i,0)+1
            
        #{3:1, 2:2,4:2} #2:[4,2] 
        buck=[[] for i in range(len(nums)+1)]
        for key,value in freq.items(): #
            buck[value].append(key)
        res=[]
        
        for i in range(len(buck)-1,0,-1):  #o(k)
            for j in buck[i]: 
                res.append(j)
                if len(res)==k:
                    return res