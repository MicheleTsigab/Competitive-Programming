class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        edge = defaultdict(list)
        inc = defaultdict(int)
        for u,v in adjacentPairs:
            edge[u].append(v)
            inc[u]+=1
            edge[v].append(u)
            inc[v]+=1
        seen = set()
        start = 0
        for i in inc:
            if inc[i] == 1:
                start = i
                break
        ans = []
        def dfs(node):
            ans.append(node)
            seen.add(node)
            for nei in edge[node]:
                if nei in seen:
                    continue
                dfs(nei)
        dfs(start)
        return ans