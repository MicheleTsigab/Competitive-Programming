# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def dfs(node, go_left,go_right):
            if not node:
                return 0
            
            g_left = 0
            if go_left:
                g_left = 1 + dfs(node.left, go_left = False, go_right = True)

            g_right = 0
            if go_right:
                g_right = 1 + dfs(node.right, go_left = True, go_right = False)
            start_left = 0
            start_right = 0
            if go_left and go_right:
                start_left = dfs(node.left, go_left = True, go_right = True)
                start_right = dfs(node.right, go_left = True, go_right = True)
            
            return max(g_left, start_left, g_right, start_right)
        return  dfs(root,True,True) - 1