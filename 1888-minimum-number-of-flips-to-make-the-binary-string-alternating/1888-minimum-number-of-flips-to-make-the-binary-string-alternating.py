class Solution:
    def minFlips(self, s: str) -> int:
        ideal_one = []
        ideal_zero = []
        s =list(s)
        n = 2 * len(s)
        for i in range(n):
            if not i%2:
                ideal_one.append('1')
                ideal_zero.append('0')
            else:
                ideal_one.append('0')
                ideal_zero.append('1')

        #first window        
        ideal_one_diff = 0
        ideal_zero_diff = 0
        for right in range(len(s)):
            if s[right]!=ideal_one[right]:
                ideal_one_diff +=1
            if s[right]!=ideal_zero[right]:
                ideal_zero_diff +=1
        #print(s,ideal_one_diff)
        #print(ideal_one)
        ans = min(ideal_one_diff,ideal_zero_diff)
        
        left = 0
        for right in range(len(s),n):
            #print(s[left],ideal_one[right],ideal_zero[right])
            if s[left]!=ideal_one[left]:
                ideal_one_diff -=1
            if s[left]!=ideal_zero[left]:
                ideal_zero_diff -= 1
            #s[-1]=s[left]
            if s[left]!=ideal_one[right]:
                ideal_one_diff += 1
            if s[left]!=ideal_zero[right]:
                ideal_zero_diff += 1
            ans = min(ans,ideal_zero_diff,ideal_one_diff)
            left += 1
        return ans