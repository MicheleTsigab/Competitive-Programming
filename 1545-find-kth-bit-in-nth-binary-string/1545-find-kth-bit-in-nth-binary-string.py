class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """ 
        s1 = "0"
              k=1
              1 2 3
        S2 = "0 1 1"
                  k
              mid = 3//2 = 1
              actual mid = 3
              k > 1 $$ k!=2
              3 - 3 + 1 = flip(1)
              123 4 567 
        S3 = "011 1 110"
                k'  k
                7 - 5 + 1 = k'
                mid = 7//2 = 3
                actual mid = 4

        """
        if n==1:
            return '0'
        length = (1 << n) - 1
        mid = length//2
        if k==mid + 1:
            return '1'
        if k <=mid:
            return self.findKthBit(n-1,k)
        else:
            k = length - k + 1
            char = self.findKthBit(n-1,k)
            if char == '1':
                return '0'
            else:
                return '1'