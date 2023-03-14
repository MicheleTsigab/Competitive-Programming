class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
       <- -2  <- -1 1 -> 2->
       
        
        """
        def different_sign(a,b):
            return (a < 0 and b > 0) or (a > 0 and b< 0)
        st = []
        
        for i in asteroids:
            flag = True
            while st and st[-1] > 0 and i<0:
                if st[-1] > -i:
                    flag = False
                    break
                removed = st.pop()
                if removed==-i:
                    flag = False
                    break
            if flag:
                st.append(i)
        return st
                