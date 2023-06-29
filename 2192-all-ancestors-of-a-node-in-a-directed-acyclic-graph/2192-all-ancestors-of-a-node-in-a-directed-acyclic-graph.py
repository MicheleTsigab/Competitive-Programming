class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        #top sort
        ans = [set() for i in range(n)]
        inc = defaultdict(int)
        q = deque()
        ed = defaultdict(list)
        for fro,to in edges:
            ed[fro].append(to)
            inc[to]+=1
        #print(inc)
        for i in range(n):
            if inc[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            for nei in ed[node]:
                ans[nei].add(node)
                for x in ans[node]:
                    ans[nei].add(x)
                inc[nei]-=1
                if inc[nei] == 0:
                    q.append(nei)
        ans = [sorted(i) for i in ans]
        return ans