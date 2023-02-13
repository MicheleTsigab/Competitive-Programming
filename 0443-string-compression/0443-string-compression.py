class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        n = len(chars)
        left,right = 0,0
        # assign to chars as suitable to the required output format and return the length
        def assign(ans, left, right): 
            chars[ans]=chars[left]
            ans += 1
            if 1 < right - left < 10:
                chars[ans]=str(right - left)
                ans+=1
            elif right - left >= 10:
                for i in str((right - left)):
                    chars[ans]=i
                    ans+=1
            return ans
        
        while right < n:
            if chars[left]!=chars[right]: #if similar characters were interupted
                ans = assign(ans,left, right)
                left = right
            right +=1    
        ans = assign(ans,left,right)
        return ans