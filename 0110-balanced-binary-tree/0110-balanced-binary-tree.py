# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        marker=True
        def dfs(node):
            nonlocal marker
            if node==None:
                return 0
            left=1+dfs(node.left)
            right=1+dfs(node.right)
            if abs(left-right)>1:
                marker=False
            return max(left,right) 
        dfs(root)
        return marker