class Solution:
    def validPalindrome(self, s: str) -> bool:
        #aa
        #abca
        #abae
        #abc
        #ae
        left = 0
        right = len(s) -1
        foul =0
        
        while left < right:
            if s[left] != s[right]:
                #check if the string a palindrom if we removed at left
                s1 = [s[i] for i in range(len(s)) if i!=right]
                #check if the string a palindrom if we removed at right
                s2 = [s[i] for i in range(len(s)) if i!=left]
                if s1[::-1]==s1 or s2[::-1]==s2:
                    return True
                return False
            left +=1
            right -=1
        return True