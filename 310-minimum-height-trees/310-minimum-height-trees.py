class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        ed = defaultdict(list)
        for u,v in edges:
            ed[u].append(v)
            ed[v].append(u)
        leaves = []
        for i in range(n):
            if len(ed[i])==1:
                leaves.append(i)
        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                nei = ed[leaf][0]
                ed[nei].remove(leaf)
                if len(ed[nei])==1:
                    new_leaves.append(nei)
            leaves = new_leaves.copy()
                    
        return leaves