class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        inc = defaultdict(int)
        ed = defaultdict(list)
        for i in range(len(graph)):
            for j in graph[i]:
                ed[j].append(i)
                inc[i]+=1
        q = deque()
        for i in range(len(graph)):
            if inc[i]==0:
                q.append(i)
        order = [False]*len(graph)
        while q:
            no = q.popleft()
            order[no] = True
            for nei in ed[no]:
                inc[nei]-=1
                if inc[nei]==0:
                    q.append(nei)
        ans = []
        for i in range(len(graph)):
            if order[i]:
                ans.append(i)
        return ans