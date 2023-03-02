class Solution:
    def compress(self, chars: List[str]) -> int:        
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
        
        length = 0 #output array length
        n = len(chars)
        left,right = 0,0
        while right < n:
            if chars[left]!=chars[right]: #if similar characters were interupted
                length = assign(length,left, right)
                left = right
            right +=1    
        length = assign(length,left,right)
        return length