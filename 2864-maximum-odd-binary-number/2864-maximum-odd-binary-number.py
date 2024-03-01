class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        one = 0
        for i in s:
            if i =='1':
                one+=1
        ans = []
        for i in range(one-1):
            ans.append('1')
        for i in range(len(s)-one):
            ans.append('0')
        ans.append('1')
        return ''.join(ans)