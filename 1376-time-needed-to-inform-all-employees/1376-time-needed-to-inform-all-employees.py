class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        for i in range(len(manager)):
            if manager[i]!=-1:
                g[manager[i]].append(i)
        
        q = deque()
        q.append([headID,0])
        seen = set()
        seen.add(headID)
        ans = 0
        while q:
            node,leng = q.popleft()
            if not g[node]:
                ans = max(leng,ans)
            for nei in g[node]:
                if nei not in seen:
                    q.append([nei,leng+informTime[node]])
                    seen.add(nei)
        return ans