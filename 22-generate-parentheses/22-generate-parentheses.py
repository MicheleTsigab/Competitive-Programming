class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def generate(op,cl,par_set):
            """
            given op and cl variables representing opening and closing number of parenthesis we have left 
            we want to decide and output correct pair of parenthesis
            rule 1. if we don't have enough op,cl meaning greater than n we can't open
            rule 2. if we didn't have enough op(opening bracket) left to close we can't close
            """
            if len(par_set)==2*n:
                res.append(''.join(par_set))
                return
            if op > 0: #rule no 1
                par_set.append('(')
                generate(op-1,cl,par_set)
                par_set.pop()
            if n - op > n-cl and cl > 0: # the brackets we have opened is greater than the brackets we have closing
                par_set.append(')')
                generate(op,cl-1,par_set)
                par_set.pop()
                
        generate(n,n,[])    
        return res
        