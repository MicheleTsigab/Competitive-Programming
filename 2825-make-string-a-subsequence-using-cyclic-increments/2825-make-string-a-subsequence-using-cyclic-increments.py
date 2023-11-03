class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """
        ch = {'a':'b','b':'c',''}
        st1 = zzc
             i
        
        st2 = ad
               j
               
        """
        
        i,j = 0,0
        alphabet1 = list(string.ascii_lowercase)
        alphabet2 = alphabet1[1:] + ['a']
        ch = {x:y for x,y in zip(alphabet1,alphabet2)}
        while i < len(str1) and j < len(str2):
            if str1[i]==str2[j] or ch[str1[i]]==str2[j]:
                j+=1
                i+=1
            else:
                i+=1
        return j==len(str2)
            