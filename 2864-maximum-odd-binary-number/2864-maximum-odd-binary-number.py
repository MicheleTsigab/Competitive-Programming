class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        one = s.count('1')
        ans = ['1']*(one-1) + ['0']*(len(s)-one) + ['1']
        # for i in range(one-1):
        #     ans.append('1')
        # for i in range(len(s)-one):
        #     ans.append('0')
        # ans.append('1')
        return ''.join(ans)