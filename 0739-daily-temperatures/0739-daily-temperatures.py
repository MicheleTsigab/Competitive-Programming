class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dec_stack = []
        ans = [0] * len(temperatures)
        for right,n in enumerate(temperatures):
            
            while dec_stack and n > temperatures[dec_stack[-1]]: 
                idx = dec_stack.pop()
                ans[idx] = right - idx
            dec_stack.append(right)
        return ans