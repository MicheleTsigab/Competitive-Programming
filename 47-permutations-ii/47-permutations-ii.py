class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)
        def search(curr):
            if len(curr)==len(nums):
                res.append(curr.copy())
            for n in count:
                if count[n] > 0:
                    count[n]-=1
                    curr.append(n)
                    search(curr)
                    count[n]+=1
                    curr.pop()
                    
        search([])
        return res