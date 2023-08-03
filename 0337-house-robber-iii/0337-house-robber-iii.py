# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @lru_cache(None)
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = root.val
        if root.right:
            ans += self.rob(root.right.left) + self.rob(root.right.right)
        if root.left:
            ans += self.rob(root.left.left) + self.rob(root.left.right)
        
        return max(ans,self.rob(root.left)+self.rob(root.right)) #decision not to include current node