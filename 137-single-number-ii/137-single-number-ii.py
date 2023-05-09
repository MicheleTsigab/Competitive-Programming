class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #have a counter m, which can count upto k-1
        one_cnt = 0 #counts if a number appears one time
        two_cnt = 0 #counts if a number appears two time
        
        for i in nums:
            one_cnt^=i
            one_cnt&=~two_cnt
            two_cnt ^= i
            two_cnt &= ~one_cnt
        return one_cnt