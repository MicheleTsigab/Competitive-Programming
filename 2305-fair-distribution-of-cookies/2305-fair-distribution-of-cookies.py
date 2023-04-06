class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        """
        8 15 10 20 8
             i
        
        [0,8] [8,0]
         x
    [0,23] [15,8] [23,0] [8,15]
        x  x 
[10,23] [0,33] [25,8] [15,18] [33,0] [23,10] [18,15] [8,25]
     x    x     x      x
        """
        cookies.sort(reverse=True)
        seen = set()
        def dist(i,bucket):
            if i == len(cookies):
                return max(bucket)
            ans = inf 
            for j in range(len(bucket)):
                bucket[j]+=cookies[i]
                x = ''.join(sorted(map(str,bucket)))
                if x not in seen:
                    seen.add(x)
                    ans = min(ans,dist(i+1,bucket))
                bucket[j]-=cookies[i]
            return ans
        bucket = [0] * k
        return dist(0,bucket)
            
                