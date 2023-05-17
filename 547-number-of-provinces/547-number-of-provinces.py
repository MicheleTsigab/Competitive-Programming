class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            
            for n in range(len(isConnected)):
                if isConnected[n][node] == 1 and n not in seen:
                    dfs(n)
        
        ans = 0
        for i in range(len(isConnected)):
            if i not in seen:
                ans+=1
                dfs(i)
        return ans