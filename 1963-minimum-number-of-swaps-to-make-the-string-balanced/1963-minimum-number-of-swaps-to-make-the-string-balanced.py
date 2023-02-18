class Solution:
    def minSwaps(self, s: str) -> int:
        """
        [[]] if at ight is opened find closed from left
        ]]][[]]
        [       ]
        "[ [ ] ]"
         l     r
                 
         open = 1
         closed = 0
         count = 1
        """
        s = list(s)
        right = len(s) - 1
        count = 0
        opened = 0
        closed = 0
        for left,c in enumerate(s):
            if c=='[':
                opened+=1
            else:
                closed+=1
            if opened >= closed:
                continue
            #closed is bigger on the left
            while right > left and s[right]!='[':
                right -=1
            
            s[left],s[right]=s[right],s[left]
            closed -= 1
            opened += 1
            right -= 1
            count +=1
        return count
            
                    