class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        x = deque()
        for i in nums:
            if i % 2:
                x.append(i)
            else:
                x.appendleft(i)
        return x