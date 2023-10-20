
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        trie = {}
        def insert(num):
            #insert bits of a num as a node to the trie from most significant
            cur = trie
            for i in range(30,-1,-1):
                bit = (num>>i)&1
                if bit not in cur:
                    cur[bit]={}
                cur = cur[bit]
        def findmax(num):
            #find the best compliment available
            cur = trie
            ans = 0
            for i in range(30,-1,-1):
                bit = (num>>i)&1
                if (1-bit) in cur:
                    #if we got complimentary go down that road,
                    #since it is the best we can form
                    cur = cur[1-bit]
                    ans |=(1<<i)

                else:
                    cur = cur[bit]
            return ans
        
        for i in nums:
            insert(i)
        ans = 0
        for i in nums:
            ans = max(ans, findmax(i))
        return ans