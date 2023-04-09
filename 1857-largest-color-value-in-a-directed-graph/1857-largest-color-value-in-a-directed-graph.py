class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        g = {i:[] for i in range(len(colors))}
        for x,y in edges:
            g[x].append(y)
   #     print(g)
        #given node find its largest color value
        def color_value(node):
            
            #iscycle
            if node in path:
                return inf
            if node in visited:
                return 0 #arbitrary num
            visited.add(node)
            path.add(node)
            idx = ord(colors[node]) - ord('a')
            node_color[node][idx] = 1
            
            for nei in g[node]:
                if color_value(nei) == inf:
                    return inf
                for i in range(26):
                    node_color[node][i] = max(
                        (1 if i==idx else 0) + node_color[nei][i],
                        node_color[node][i])
            path.remove(node)
            return max(node_color[node])
        visited, path = set(), set()
        node_color = [[0 for i in range(26)] for _ in range(len(colors))]
        ans = 0
        
        for i in range(len(colors)):
            ans = max(ans,color_value(i))
        
        return ans if ans!=inf else -1