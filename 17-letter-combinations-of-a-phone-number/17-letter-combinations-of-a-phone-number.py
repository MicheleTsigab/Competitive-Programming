class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        digit_map={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        n=len(digits)
        res=[]
        def search(i,comb_set):
            if len(comb_set)==n:
                temp=''.join(comb_set)
                res.append(temp)
                return
            for letter in digit_map[digits[i]]:
                comb_set.append(letter)
                search(i+1,comb_set)
                comb_set.pop()
        search(0,[])

                        
        return res