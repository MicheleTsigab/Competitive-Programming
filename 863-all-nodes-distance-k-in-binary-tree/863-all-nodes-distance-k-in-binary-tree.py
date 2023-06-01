# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        if k == 0:
            return [target.val]
        
        def dfs(node):
            if not node:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)
        dfs(root)
        #print(graph)
        q = deque()
        q.append([target.val,0])
        seen = set()
        seen.add(target)
        ans = []
        while q:
            node,length = q.popleft()
            #print(node,length)
            if node!=target.val and length == k:
                ans.append(node)
            for nei in graph[node]:
                if nei not in seen:
                    q.append([nei,length+1])
                    seen.add(nei)
        return ans
                    