class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """
        ch = {'a':'b','b':'c',''}
        st1 = zzc
             i
        
        st2 = ad
               j
               
        """
        #o(N+M)
        #o(26)
        i,j = 0,0
        alphabet1 = list(string.ascii_lowercase)
        alphabet2 = alphabet1[1:] + ['a']
        ch = {x:y for x,y in zip(alphabet1,alphabet2)}
        while i < len(str1) and j < len(str2):
            if str1[i]==str2[j] or (ord(str1[i])-ord('a')+1)%26==ord(str2[j])-ord('a'):
                j+=1
                i+=1
            else:
                i+=1
        return j==len(str2)
            