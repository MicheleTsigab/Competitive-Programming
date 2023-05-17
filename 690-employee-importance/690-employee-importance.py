"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        g = defaultdict(list)
        ut = defaultdict(int)
        
        for i in employees:
            g[i.id] = list(i.subordinates)
            ut[i.id] = i.importance
        seen = set()
        def dfs(node):
            if node in seen:
                return 0
            seen.add(node)
            ans = ut[node]
 
            for nei in g[node]:
                
                if nei not in seen:
                    ans+=dfs(nei)
            return ans
        return dfs(id)