class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_set = set(nums)
        m= len(nums[0])
        
        def search(curr):
            if len(curr)==m:
                st=''.join(curr)
                if st not in nums_set:
                    return st
                return None
            curr.append('0')
            find=search(curr)
            curr.pop()
            if find:
                return find
            
            curr.append('1')
            find= search(curr)
            curr.pop()
            if find:
                return find
        
        return search([])
            