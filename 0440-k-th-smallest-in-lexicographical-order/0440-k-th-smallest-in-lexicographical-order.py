class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def count_nums_interval(n1):
            n2 = n1 + 1
            steps = 0
            while n1 <= n: 
                steps += (min(n+1,n2)- n1)
                n1 *=10
                n2*=10
            return steps
        curr = 1
        
        while k>1:
            #gets numbers between two numbers on the same level curr and curr + 1
            count = count_nums_interval(curr)
            if k > count:#ignore this range because we want a number greater than those in this interval
                k-=count
                curr +=1
            else:
                #fix the prefix that starts with curr and find the remaing digits
                curr *=10
                k-=1
        return curr
                