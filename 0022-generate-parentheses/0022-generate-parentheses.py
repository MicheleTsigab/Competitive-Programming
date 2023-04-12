class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        3 3
        
        """
        res = []

        def generate(op,cl,path):
            if not op and not cl:
                res.append(''.join(path))
                return
            
            if op > 0:
                generate(op-1,cl,path + ['('])
            if n - op > n - cl and cl > 0:
                generate(op,cl-1,path + [')'])
        generate(n,n,[])
        return res