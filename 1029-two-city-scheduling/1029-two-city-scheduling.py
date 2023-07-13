class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        
        if diff between costb - costa is positive, it means the ith person should go to city A,
        because costa is less expensive than costb
        """
        costs.sort(key = lambda a:a[1]-a[0],reverse = True)
        cnt = 0
        n = len(costs)/2
        ans = 0
        for a,b in costs:
            if cnt < n:
                ans += a
            else:
                ans += b
            cnt += 1
        return ans